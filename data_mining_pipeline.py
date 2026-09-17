
"""Run the complete rule-mining and classification workflow.

This portfolio version preserves the analysis completed for CSCI 7434 while
replacing course-environment file paths with command-line arguments. The
professor-provided dataset is not included in the public repository.
"""

from __future__ import annotations

import argparse
import math
from collections import Counter
from itertools import combinations
from pathlib import Path
from typing import Dict, List, Tuple, Iterable, FrozenSet, Any

import numpy as np
import pandas as pd


CONFIG = {
    "correlation_threshold": 0.70,
    "confidence_threshold": 0.70,
    "minimum_support_count": 17,
    "random_seed": 100,
    "test_fraction": 0.10,
    "round_test_sample_up": True,
    "no_match_prediction": 0,
    "conflict_resolution": "highest_confidence_then_longest_antecedent",
    "diff_round_decimals": 1,
    "population_std": True,
}


def parse_arguments() -> argparse.Namespace:
    """Collect file locations without tying the pipeline to one computer."""
    parser = argparse.ArgumentParser(
        description="Run the end-to-end association-rule classification pipeline."
    )
    parser.add_argument(
        "--input",
        required=True,
        type=Path,
        help="Path to a CSV file containing a binary 'treat' column and numeric features.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("outputs"),
        help="Directory for generated CSV and JSON audit files (default: outputs).",
    )
    return parser.parse_args()


def validate_input_data(df: pd.DataFrame) -> List[str]:
    """Validate the minimum schema assumptions used throughout the pipeline."""
    if "treat" not in df.columns:
        raise ValueError("Input data must include a binary 'treat' column.")

    independent_attributes = [column for column in df.columns if column != "treat"]
    if not independent_attributes:
        raise ValueError("Input data must include at least one independent attribute.")
    if df.empty:
        raise ValueError("Input data cannot be empty.")
    if df.isna().any().any():
        raise ValueError("Input data contains missing values; clean or impute them before running.")

    non_numeric = [
        column for column in df.columns if not pd.api.types.is_numeric_dtype(df[column])
    ]
    if non_numeric:
        raise ValueError(f"All columns must be numeric. Non-numeric columns: {non_numeric}")

    treat_values = set(df["treat"].unique().tolist())
    if not treat_values.issubset({0, 1}):
        raise ValueError("The 'treat' column must contain only 0 and 1 values.")

    return independent_attributes


def explain_function_purpose() -> Dict[str, str]:
    return {
        "compute_attribute_statistics": "Calculates AVG, population STD, lower bound, upper bound, and outlier counts for each independent attribute.",
        "mark_outliers_and_clean": "Flags outlier rows and removes any record that contains at least one outlier.",
        "build_correlation_matrix": "Builds the Pearson correlation matrix on the cleaned independent attributes and identifies any pair above the chosen threshold.",
        "build_diff_union": "Builds the Diff_Union candidate set by sorting values, computing adjacent differences, selecting the three largest differences, and collecting the responsible values.",
        "choose_best_entropy_threshold": "Tests only Diff_Union candidate thresholds and keeps the threshold with maximum information gain.",
        "discretize_dataset": "Converts each continuous independent attribute into a binary discrete attribute using the chosen entropy threshold.",
        "split_train_test": "Creates Econ-TEST and Econ-TRAIN from the fully discretized Economy dataset using a reproducible, class-stratified random split.",
        "build_table_a_and_transactions": "Creates Table A, renames discrete values to I-labels, and converts Econ-TRAIN and Econ-TEST into item transactions for Apriori.",
        "apriori_frequent_itemsets": "Runs Apriori level by level using the user-selected minimum support count.",
        "generate_association_rules": "Generates association rules from the valid frequent itemsets and computes confidence for each rule.",
        "predict_test_records": "Applies Format-1-Rules to Econ-TEST and produces one binary prediction per record using a documented tie-breaking/default strategy.",
        "calculate_metrics": "Builds the TP/FN/FP/TN matrix and calculates Accuracy, Recall, and Precision."
    }


def entropy_of_labels(labels: Iterable[int]) -> float:
    labels = list(labels)
    if not labels:
        return 0.0
    counts = Counter(labels)
    total = len(labels)
    entropy = 0.0
    for count in counts.values():
        probability = count / total
        entropy -= probability * math.log2(probability)
    return entropy


def compute_attribute_statistics(df: pd.DataFrame, independent_attributes: List[str]) -> Tuple[pd.DataFrame, Dict[str, Dict[str, Any]]]:
    records = []
    details = {}
    ddof = 0
    for attribute in independent_attributes:
        avg = df[attribute].mean()
        std = df[attribute].std(ddof=ddof)
        lower_bound = avg - 2 * std
        upper_bound = avg + 2 * std
        outlier_mask = (df[attribute] < lower_bound) | (df[attribute] > upper_bound)
        outlier_values = sorted(df.loc[outlier_mask, attribute].unique().tolist())
        records.append({
            "Attribute": attribute,
            "AVG": avg,
            "STD": std,
            "Lower Bound (AVG-2*STD)": lower_bound,
            "Upper Bound (AVG+2*STD)": upper_bound,
            "Outlier Count": int(outlier_mask.sum()),
            "Outlier Values": ", ".join(f"{value:.1f}" for value in outlier_values) if outlier_values else "None",
        })
        details[attribute] = {
            "avg": avg,
            "std": std,
            "lower_bound": lower_bound,
            "upper_bound": upper_bound,
            "outlier_mask": outlier_mask,
            "outlier_values": outlier_values,
        }
    return pd.DataFrame(records), details


def mark_outliers_and_clean(df: pd.DataFrame, independent_attributes: List[str], stats_details: Dict[str, Dict[str, Any]]) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    combined_mask = pd.Series(False, index=df.index)
    row_reasons = []
    for attribute in independent_attributes:
        combined_mask |= stats_details[attribute]["outlier_mask"]

    removed_df = df.loc[combined_mask].copy()
    kept_df = df.loc[~combined_mask].copy().reset_index(drop=True)

    for original_index, row in removed_df.iterrows():
        reasons = []
        for attribute in independent_attributes:
            value = row[attribute]
            lower = stats_details[attribute]["lower_bound"]
            upper = stats_details[attribute]["upper_bound"]
            if value < lower or value > upper:
                reasons.append(f"{attribute}={value:.1f} outside [{lower:.3f}, {upper:.3f}]")
        row_reasons.append({
            "Original Row Number (1-based data row)": int(original_index) + 1,
            "Reasons": " | ".join(reasons)
        })

    removed_report = removed_df.reset_index().rename(columns={"index": "Original Row Index"})
    removed_report["Original Row Number (1-based data row)"] = removed_report["Original Row Index"] + 1
    reason_df = pd.DataFrame(row_reasons)
    removed_report = removed_report.merge(reason_df, on="Original Row Number (1-based data row)", how="left")
    return kept_df, removed_report, pd.DataFrame({"Removed Record Count": [int(combined_mask.sum())], "Remaining Record Count": [len(kept_df)]})


def build_correlation_matrix(clean_df: pd.DataFrame, independent_attributes: List[str], threshold: float) -> Tuple[pd.DataFrame, pd.DataFrame]:
    correlation_matrix = clean_df[independent_attributes].corr(method="pearson")
    high_pairs = []
    for i, left_attr in enumerate(independent_attributes):
        for right_attr in independent_attributes[i + 1:]:
            coefficient = correlation_matrix.loc[left_attr, right_attr]
            if abs(coefficient) > threshold:
                high_pairs.append({
                    "Attribute A": left_attr,
                    "Attribute B": right_attr,
                    "Pearson Correlation": coefficient,
                    "Above Threshold": True,
                })
    high_pair_df = pd.DataFrame(high_pairs) if high_pairs else pd.DataFrame(columns=["Attribute A", "Attribute B", "Pearson Correlation", "Above Threshold"])
    return correlation_matrix, high_pair_df


def build_diff_union(series: pd.Series, diff_round_decimals: int = 1) -> Dict[str, Any]:
    unique_desc = sorted(pd.unique(series), reverse=True)
    diff_rows = []
    for position in range(len(unique_desc) - 1):
        high_value = float(unique_desc[position])
        low_value = float(unique_desc[position + 1])
        difference = round(high_value - low_value, diff_round_decimals)
        diff_rows.append({
            "High Value": high_value,
            "Low Value": low_value,
            "Difference": difference,
            "Value Responsible (Lower Value)": low_value,
        })
    diff_df = pd.DataFrame(diff_rows)
    diff_sorted = diff_df.sort_values(["Difference", "Value Responsible (Lower Value)"], ascending=[False, False]).reset_index(drop=True)
    top_three_rows = diff_sorted.head(3).copy()
    top_three_difference_values = sorted(top_three_rows["Difference"].unique().tolist(), reverse=True)
    diff_union_values = sorted(diff_df.loc[diff_df["Difference"].isin(top_three_difference_values), "Value Responsible (Lower Value)"].unique().tolist())
    return {
        "sorted_unique_values_desc": unique_desc,
        "adjacent_differences": diff_df,
        "top_three_difference_rows": top_three_rows,
        "top_three_difference_values": top_three_difference_values,
        "diff_union": diff_union_values,
    }


def choose_best_entropy_threshold(clean_df: pd.DataFrame, attribute: str, diff_union_payload: Dict[str, Any]) -> Dict[str, Any]:
    total_entropy = entropy_of_labels(clean_df["treat"].tolist())
    evaluation_rows = []
    for threshold in diff_union_payload["diff_union"]:
        left_partition = clean_df.loc[clean_df[attribute] < threshold, "treat"].tolist()
        right_partition = clean_df.loc[clean_df[attribute] >= threshold, "treat"].tolist()
        left_entropy = entropy_of_labels(left_partition)
        right_entropy = entropy_of_labels(right_partition)
        weighted_entropy = (
            (len(left_partition) / len(clean_df)) * left_entropy
            + (len(right_partition) / len(clean_df)) * right_entropy
        )
        information_gain = total_entropy - weighted_entropy
        evaluation_rows.append({
            "Attribute": attribute,
            "Threshold": threshold,
            "Left Partition Rule": f"{attribute} < {threshold}",
            "Right Partition Rule": f"{attribute} >= {threshold}",
            "Left Count": len(left_partition),
            "Right Count": len(right_partition),
            "Left Entropy": left_entropy,
            "Right Entropy": right_entropy,
            "Weighted Entropy": weighted_entropy,
            "Information Gain": information_gain,
        })
    evaluation_df = pd.DataFrame(evaluation_rows).sort_values(["Information Gain", "Threshold"], ascending=[False, True]).reset_index(drop=True)
    best_row = evaluation_df.iloc[0].to_dict()
    return {
        "attribute": attribute,
        "diff_union_payload": diff_union_payload,
        "evaluation_df": evaluation_df,
        "best_threshold": best_row["Threshold"],
        "best_information_gain": best_row["Information Gain"],
    }


def discretize_dataset(clean_df: pd.DataFrame, independent_attributes: List[str], thresholds: Dict[str, float]) -> pd.DataFrame:
    discretized = clean_df.copy()
    for attribute in independent_attributes:
        threshold = thresholds[attribute]
        discretized[attribute] = np.where(clean_df[attribute] < threshold, 1, 2)
    return discretized


def split_train_test(discretized_df: pd.DataFrame, random_seed: int, test_fraction: float, round_up: bool) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    rng = np.random.RandomState(random_seed)
    test_indices: List[int] = []
    split_rows = []
    for treat_value, group_df in discretized_df.groupby("treat"):
        raw_count = len(group_df) * test_fraction
        sample_count = math.ceil(raw_count) if round_up else int(round(raw_count))
        chosen_indices = rng.choice(group_df.index.to_list(), size=sample_count, replace=False)
        test_indices.extend(chosen_indices.tolist())
        split_rows.append({
            "treat": int(treat_value),
            "Discretized Class Count": len(group_df),
            "10% Raw Value": raw_count,
            "Sampling Rule": "Round up to guarantee at least 10% from each class" if round_up else "Round to nearest whole number",
            "Econ-TEST Sample Count": int(sample_count),
        })

    econ_test = discretized_df.loc[sorted(test_indices)].copy().reset_index(drop=True)
    econ_train = discretized_df.drop(index=test_indices).copy().reset_index(drop=True)
    split_df = pd.DataFrame(split_rows).sort_values("treat").reset_index(drop=True)
    return econ_train, econ_test, split_df


def build_table_a_and_transactions(
    clean_numeric_df: pd.DataFrame,
    discretized_reference_df: pd.DataFrame,
    econ_train: pd.DataFrame,
    econ_test: pd.DataFrame,
    thresholds: Dict[str, float],
    all_attributes: List[str],
) -> Tuple[pd.DataFrame, Dict[Tuple[str, int], str], List[Tuple[str, ...]], List[Tuple[str, ...]], Dict[str, str], Dict[str, int], Dict[str, str]]:
    table_rows = []
    attribute_value_to_item: Dict[Tuple[str, int], str] = {}
    item_to_attribute: Dict[str, str] = {}
    item_to_discrete_value: Dict[str, int] = {}
    item_to_range: Dict[str, str] = {}
    counter = 1

    for attribute in all_attributes:
        if attribute == "treat":
            for value in sorted(discretized_reference_df[attribute].unique().tolist()):
                item_name = f"I{counter}"
                counter += 1
                value = int(value)
                value_range = str(value)
                table_rows.append({
                    "Attribute Name": attribute,
                    "Discrete Value": value,
                    "Naming": item_name,
                    "Range": value_range,
                })
                attribute_value_to_item[(attribute, value)] = item_name
                item_to_attribute[item_name] = attribute
                item_to_discrete_value[item_name] = value
                item_to_range[item_name] = value_range
        else:
            threshold = thresholds[attribute]
            minimum = clean_numeric_df[attribute].min()
            maximum = clean_numeric_df[attribute].max()
            ranges = {
                1: f"[{minimum:.1f}-{threshold:.1f})",
                2: f"[{threshold:.1f}-{maximum:.1f}]",
            }
            for value in [1, 2]:
                item_name = f"I{counter}"
                counter += 1
                table_rows.append({
                    "Attribute Name": attribute,
                    "Discrete Value": value,
                    "Naming": item_name,
                    "Range": ranges[value],
                })
                attribute_value_to_item[(attribute, value)] = item_name
                item_to_attribute[item_name] = attribute
                item_to_discrete_value[item_name] = value
                item_to_range[item_name] = ranges[value]

    table_a = pd.DataFrame(table_rows)

    def to_transactions(discrete_df: pd.DataFrame) -> List[Tuple[str, ...]]:
        transactions = []
        for _, row in discrete_df.iterrows():
            transaction_items = tuple(attribute_value_to_item[(attribute, int(row[attribute]))] for attribute in all_attributes)
            transactions.append(transaction_items)
        return transactions

    train_transactions = to_transactions(econ_train)
    test_transactions = to_transactions(econ_test)

    return table_a, attribute_value_to_item, train_transactions, test_transactions, item_to_attribute, item_to_discrete_value, item_to_range


def apriori_frequent_itemsets(transactions: List[Tuple[str, ...]], min_support_count: int) -> Dict[int, Dict[FrozenSet[str], int]]:
    transaction_sets = [frozenset(transaction) for transaction in transactions]

    item_counts = Counter()
    for transaction in transaction_sets:
        for item in transaction:
            item_counts[frozenset([item])] += 1

    levels: Dict[int, Dict[FrozenSet[str], int]] = {}
    level_one = {itemset: count for itemset, count in item_counts.items() if count >= min_support_count}
    levels[1] = dict(sorted(level_one.items(), key=lambda pair: tuple(sorted(pair[0]))))

    k = 2
    while levels.get(k - 1):
        previous_itemsets = list(levels[k - 1].keys())
        previous_sorted_tuples = [tuple(sorted(itemset)) for itemset in previous_itemsets]
        previous_set = set(previous_itemsets)
        candidates = set()

        for left_index in range(len(previous_sorted_tuples)):
            for right_index in range(left_index + 1, len(previous_sorted_tuples)):
                left_tuple = previous_sorted_tuples[left_index]
                right_tuple = previous_sorted_tuples[right_index]
                if left_tuple[: k - 2] == right_tuple[: k - 2]:
                    candidate = frozenset(set(left_tuple) | set(right_tuple))
                    if len(candidate) == k:
                        if all(frozenset(subset) in previous_set for subset in combinations(candidate, k - 1)):
                            candidates.add(candidate)
                else:
                    break

        candidate_counts = Counter()
        for transaction in transaction_sets:
            for candidate in candidates:
                if candidate.issubset(transaction):
                    candidate_counts[candidate] += 1

        frequent_candidates = {candidate: count for candidate, count in candidate_counts.items() if count >= min_support_count}
        if not frequent_candidates:
            break

        levels[k] = dict(sorted(frequent_candidates.items(), key=lambda pair: tuple(sorted(pair[0]))))
        k += 1

    return levels


def invalid_itemset_reason(itemset: FrozenSet[str], item_to_attribute: Dict[str, str]) -> str:
    attribute_counts = Counter(item_to_attribute[item] for item in itemset)
    duplicates = [attribute for attribute, count in attribute_counts.items() if count > 1]
    if not duplicates:
        return ""
    duplicate_text = ", ".join(sorted(duplicates))
    return f"More than one value from the same attribute found: {duplicate_text}"


def flatten_frequent_itemsets(levels: Dict[int, Dict[FrozenSet[str], int]], item_to_attribute: Dict[str, str]) -> Tuple[pd.DataFrame, pd.DataFrame]:
    frequent_rows = []
    removed_rows = []
    for level, itemsets in levels.items():
        for itemset, support_count in itemsets.items():
            reason = invalid_itemset_reason(itemset, item_to_attribute)
            row = {
                "Level": level,
                "Itemset": ", ".join(sorted(itemset)),
                "Support Count": support_count,
                "Is Valid": "No" if reason else "Yes",
            }
            frequent_rows.append(row)
            if reason:
                removed_rows.append({
                    "Level": level,
                    "Removed Itemset": ", ".join(sorted(itemset)),
                    "Reason": reason,
                })
    frequent_df = pd.DataFrame(frequent_rows)
    removed_df = pd.DataFrame(removed_rows) if removed_rows else pd.DataFrame(columns=["Level", "Removed Itemset", "Reason"])
    return frequent_df, removed_df


def support_count(transaction_sets: List[FrozenSet[str]], itemset: FrozenSet[str]) -> int:
    return sum(1 for transaction in transaction_sets if itemset.issubset(transaction))


def generate_association_rules(
    levels: Dict[int, Dict[FrozenSet[str], int]],
    transactions: List[Tuple[str, ...]],
    item_to_attribute: Dict[str, str],
    item_to_discrete_value: Dict[str, int],
    item_to_range: Dict[str, str],
    all_attributes: List[str],
    confidence_threshold: float,
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    transaction_sets = [frozenset(transaction) for transaction in transactions]
    frequent_itemsets = {}
    for level, level_itemsets in levels.items():
        if level >= 2:
            frequent_itemsets.update(level_itemsets)

    rules = []
    for itemset, full_support_count in frequent_itemsets.items():
        items = sorted(itemset)
        for antecedent_size in range(1, len(items)):
            for antecedent_tuple in combinations(items, antecedent_size):
                antecedent = frozenset(antecedent_tuple)
                consequent = itemset - antecedent
                antecedent_support_count = support_count(transaction_sets, antecedent)
                confidence = full_support_count / antecedent_support_count if antecedent_support_count else 0.0
                rules.append({
                    "Frequent Itemset": ", ".join(sorted(itemset)),
                    "Itemset Support Count": full_support_count,
                    "Antecedent": ", ".join(sorted(antecedent)),
                    "Consequent": ", ".join(sorted(consequent)),
                    "Antecedent Support Count": antecedent_support_count,
                    "Confidence": confidence,
                    "Antecedent Itemset": antecedent,
                    "Consequent Itemset": consequent,
                })

    rules_df = pd.DataFrame(rules)
    surviving_rules_df = rules_df.loc[rules_df["Confidence"] >= confidence_threshold].copy().reset_index(drop=True)

    attribute_order = {attribute: position for position, attribute in enumerate(all_attributes)}

    def ordered_rule_text(itemset: FrozenSet[str], use_range: bool) -> str:
        ordered_items = sorted(itemset, key=lambda item: (attribute_order[item_to_attribute[item]], item_to_discrete_value[item]))
        pieces = []
        for item in ordered_items:
            attribute = item_to_attribute[item]
            if use_range:
                pieces.append(f"{attribute} {item_to_range[item]}")
            else:
                pieces.append(f"{attribute} = {item_to_discrete_value[item]}")
        return " ∧ ".join(pieces)

    format_rows = []
    for _, row in surviving_rules_df.iterrows():
        antecedent = row["Antecedent Itemset"]
        consequent = row["Consequent Itemset"]
        format1 = f"{ordered_rule_text(antecedent, use_range=False)} => {ordered_rule_text(consequent, use_range=False)} (confidence = {row['Confidence'] * 100:.2f}%)"
        format2 = f"{ordered_rule_text(antecedent, use_range=True)} => {ordered_rule_text(consequent, use_range=True)} (confidence = {row['Confidence'] * 100:.2f}%)"
        format_rows.append({
            "Frequent Itemset": row["Frequent Itemset"],
            "Antecedent": row["Antecedent"],
            "Consequent": row["Consequent"],
            "Confidence": row["Confidence"],
            "Format-1": format1,
            "Format-2": format2,
            "Consequent Predicate Count": len(consequent),
            "Consequent Attribute": item_to_attribute[next(iter(consequent))] if len(consequent) == 1 else "Multiple",
        })

    formats_df = pd.DataFrame(format_rows).sort_values(["Confidence", "Frequent Itemset", "Antecedent"], ascending=[False, True, True]).reset_index(drop=True)
    format1_rules = formats_df.loc[(formats_df["Consequent Predicate Count"] == 1) & (formats_df["Consequent Attribute"] == "treat")].copy().reset_index(drop=True)
    return rules_df, formats_df, format1_rules


def predict_test_records(
    econ_test: pd.DataFrame,
    format1_rules: pd.DataFrame,
    attribute_value_to_item: Dict[Tuple[str, int], str],
    all_attributes: List[str],
    no_match_prediction: int,
) -> pd.DataFrame:
    working_rules = []
    for _, row in format1_rules.iterrows():
        antecedent_items = frozenset(item.strip() for item in row["Antecedent"].split(","))
        consequent_items = frozenset(item.strip() for item in row["Consequent"].split(","))
        predicted_value = int(row["Format-1"].split("=>")[1].split("=")[1].split("(")[0].strip())
        working_rules.append({
            "antecedent_items": antecedent_items,
            "predicted_treat": predicted_value,
            "confidence": row["Confidence"],
            "antecedent_length": len(antecedent_items),
            "format1": row["Format-1"],
            "format2": row["Format-2"],
        })

    working_rules.sort(key=lambda rule: (rule["confidence"], rule["antecedent_length"], rule["format1"]), reverse=True)

    prediction_rows = []
    for row_number, (_, row) in enumerate(econ_test.iterrows(), start=1):
        transaction_items = frozenset(attribute_value_to_item[(attribute, int(row[attribute]))] for attribute in all_attributes)
        matches = [rule for rule in working_rules if rule["antecedent_items"].issubset(transaction_items)]
        if matches:
            chosen_rule = matches[0]
            predicted_treat = chosen_rule["predicted_treat"]
            chosen_format1 = chosen_rule["format1"]
            chosen_format2 = chosen_rule["format2"]
        else:
            predicted_treat = no_match_prediction
            chosen_format1 = f"No rule matched -> default predict treat = {no_match_prediction}"
            chosen_format2 = f"No rule matched -> default predict treat = {no_match_prediction}"

        prediction_rows.append({
            "Test Row Number": row_number,
            "Actual treat": int(row["treat"]),
            "Predicted treat": int(predicted_treat),
            "Matched Rule Count": len(matches),
            "Chosen Rule (Format-1)": chosen_format1,
            "Chosen Rule (Format-2)": chosen_format2,
            **{attribute: int(row[attribute]) for attribute in all_attributes},
        })

    return pd.DataFrame(prediction_rows)


def calculate_metrics(prediction_df: pd.DataFrame) -> pd.DataFrame:
    actual = prediction_df["Actual treat"]
    predicted = prediction_df["Predicted treat"]
    tp = int(((actual == 1) & (predicted == 1)).sum())
    fn = int(((actual == 1) & (predicted == 0)).sum())
    fp = int(((actual == 0) & (predicted == 1)).sum())
    tn = int(((actual == 0) & (predicted == 0)).sum())

    accuracy = (tp + tn) / (tp + fn + fp + tn)
    recall = tp / (tp + fn) if (tp + fn) else 0.0
    precision = tp / (tp + fp) if (tp + fp) else 0.0

    return pd.DataFrame([
        {
            "TP (X)": tp,
            "FN (Y)": fn,
            "FP (Z)": fp,
            "TN (W)": tn,
            "Accuracy": accuracy,
            "Recall": recall,
            "Precision": precision,
            "Accuracy Formula": f"({tp} + {tn}) / ({tp} + {fn} + {fp} + {tn})",
            "Recall Formula": f"{tp} / ({tp} + {fn})" if (tp + fn) else "Undefined",
            "Precision Formula": f"{tp} / ({tp} + {fp})" if (tp + fp) else "Undefined",
        }
    ])


def support_scan_summary(transactions: List[Tuple[str, ...]], all_attributes: List[str], item_to_attribute: Dict[str, str], item_to_discrete_value: Dict[str, int], item_to_range: Dict[str, str]) -> pd.DataFrame:
    rows = []
    for minimum_support_count in range(3, 21):
        levels = apriori_frequent_itemsets(transactions, minimum_support_count)
        level_counts = {level: len(itemsets) for level, itemsets in levels.items()}
        _, formats_df, format1_rules = generate_association_rules(
            levels=levels,
            transactions=transactions,
            item_to_attribute=item_to_attribute,
            item_to_discrete_value=item_to_discrete_value,
            item_to_range=item_to_range,
            all_attributes=all_attributes,
            confidence_threshold=CONFIG["confidence_threshold"],
        )
        rows.append({
            "Minimum Support Count": minimum_support_count,
            "Total Frequent Itemsets": sum(level_counts.values()),
            "Frequent 3-Itemsets": level_counts.get(3, 0),
            "Maximum Frequent Itemset Length": max(level_counts) if level_counts else 0,
            "Surviving Format-1 Rules with treat Conclusion": len(format1_rules),
        })
    return pd.DataFrame(rows)


def main() -> None:
    args = parse_arguments()
    input_path = args.input.expanduser().resolve()
    output_dir = args.output_dir.expanduser().resolve()

    if not input_path.is_file():
        raise FileNotFoundError(f"Input CSV not found: {input_path}")

    output_dir.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(input_path)
    all_attributes = df.columns.tolist()
    independent_attributes = validate_input_data(df)

    attribute_stats_df, stats_details = compute_attribute_statistics(df, independent_attributes)
    clean_df, removed_records_df, removal_counts_df = mark_outliers_and_clean(df, independent_attributes, stats_details)

    correlation_matrix_df, high_pairs_df = build_correlation_matrix(clean_df, independent_attributes, CONFIG["correlation_threshold"])

    discretization_payloads = {}
    thresholds = {}
    discretization_summary_rows = []
    diff_union_rows = []
    threshold_evaluation_rows = []

    for attribute in independent_attributes:
        diff_union_payload = build_diff_union(clean_df[attribute], CONFIG["diff_round_decimals"])
        threshold_payload = choose_best_entropy_threshold(clean_df, attribute, diff_union_payload)
        discretization_payloads[attribute] = threshold_payload
        thresholds[attribute] = threshold_payload["best_threshold"]
        discretization_summary_rows.append({
            "Attribute": attribute,
            "Best Threshold": threshold_payload["best_threshold"],
            "Best Information Gain": threshold_payload["best_information_gain"],
            "Diff_Union": ", ".join(f"{value:.1f}" for value in diff_union_payload["diff_union"]),
            "Top Difference Values": ", ".join(str(value) for value in diff_union_payload["top_three_difference_values"]),
        })
        for value in diff_union_payload["diff_union"]:
            diff_union_rows.append({"Attribute": attribute, "Diff_Union Candidate": value})
        threshold_evaluation_df = threshold_payload["evaluation_df"].copy()
        threshold_evaluation_rows.append(threshold_evaluation_df)

    discretized_df = discretize_dataset(clean_df, independent_attributes, thresholds)
    econ_train, econ_test, split_df = split_train_test(
        discretized_df=discretized_df,
        random_seed=CONFIG["random_seed"],
        test_fraction=CONFIG["test_fraction"],
        round_up=CONFIG["round_test_sample_up"],
    )

    table_a_df, attribute_value_to_item, train_transactions, test_transactions, item_to_attribute, item_to_discrete_value, item_to_range = build_table_a_and_transactions(
        clean_numeric_df=clean_df,
        discretized_reference_df=discretized_df,
        econ_train=econ_train,
        econ_test=econ_test,
        thresholds=thresholds,
        all_attributes=all_attributes,
    )

    support_scan_df = support_scan_summary(
        transactions=train_transactions,
        all_attributes=all_attributes,
        item_to_attribute=item_to_attribute,
        item_to_discrete_value=item_to_discrete_value,
        item_to_range=item_to_range,
    )

    levels = apriori_frequent_itemsets(train_transactions, CONFIG["minimum_support_count"])
    frequent_itemsets_df, removed_invalid_df = flatten_frequent_itemsets(levels, item_to_attribute)

    rules_df, formats_df, format1_rules_df = generate_association_rules(
        levels=levels,
        transactions=train_transactions,
        item_to_attribute=item_to_attribute,
        item_to_discrete_value=item_to_discrete_value,
        item_to_range=item_to_range,
        all_attributes=all_attributes,
        confidence_threshold=CONFIG["confidence_threshold"],
    )

    train_class_counts = econ_train["treat"].value_counts().to_dict()
    ir_value = abs(train_class_counts.get(1, 0) - train_class_counts.get(0, 0)) / len(econ_train)
    balance_df = pd.DataFrame([{
        "Econ-TRAIN treat = 1 Count": train_class_counts.get(1, 0),
        "Econ-TRAIN treat = 0 Count": train_class_counts.get(0, 0),
        "IR": ir_value,
        "Dataset Status": "Imbalanced" if ir_value > 0.4 else "Balanced",
        "Rule Score Used": "Kulczynski confidence (Kulc)" if ir_value > 0.4 else "Confidence",
    }])

    prediction_df = predict_test_records(
        econ_test=econ_test,
        format1_rules=format1_rules_df,
        attribute_value_to_item=attribute_value_to_item,
        all_attributes=all_attributes,
        no_match_prediction=CONFIG["no_match_prediction"],
    )
    metrics_df = calculate_metrics(prediction_df)

    function_purpose_df = pd.DataFrame(list(explain_function_purpose().items()), columns=["Function", "Purpose"])
    thresholds_df = pd.DataFrame([
        {"Setting": "Correlation Threshold", "Value": CONFIG["correlation_threshold"]},
        {"Setting": "Confidence Threshold", "Value": CONFIG["confidence_threshold"]},
        {"Setting": "Minimum Support Count", "Value": CONFIG["minimum_support_count"]},
        {"Setting": "Random Seed", "Value": CONFIG["random_seed"]},
        {"Setting": "Round Test Sample Up", "Value": CONFIG["round_test_sample_up"]},
        {"Setting": "No-Match Prediction", "Value": CONFIG["no_match_prediction"]},
    ])

    threshold_evaluations_combined_df = pd.concat(threshold_evaluation_rows, ignore_index=True)
    discretization_summary_df = pd.DataFrame(discretization_summary_rows)
    diff_union_df = pd.DataFrame(diff_union_rows)
    train_transactions_df = pd.DataFrame({"Transaction ID": range(1, len(train_transactions) + 1), "Items": [", ".join(transaction) for transaction in train_transactions]})
    test_transactions_df = pd.DataFrame({"Transaction ID": range(1, len(test_transactions) + 1), "Items": [", ".join(transaction) for transaction in test_transactions]})

    outputs = {
        "01_function_purposes.csv": function_purpose_df,
        "02_locked_settings.csv": thresholds_df,
        "03_part1_attribute_statistics.csv": attribute_stats_df,
        "04_part1_removed_outlier_records.csv": removed_records_df,
        "05_part1_removal_counts.csv": removal_counts_df,
        "06_part1_correlation_matrix.csv": correlation_matrix_df,
        "07_part1_high_correlation_pairs.csv": high_pairs_df,
        "08_part1_diff_union_candidates.csv": diff_union_df,
        "09_part1_threshold_evaluations.csv": threshold_evaluations_combined_df,
        "10_part1_discretization_summary.csv": discretization_summary_df,
        "11_part1_discretized_economy.csv": discretized_df,
        "12_part2_split_summary.csv": split_df,
        "13_part2_econ_train.csv": econ_train,
        "14_part2_econ_test.csv": econ_test,
        "15_part2_table_a.csv": table_a_df,
        "16_part2_train_transactions.csv": train_transactions_df,
        "17_part2_test_transactions.csv": test_transactions_df,
        "18_part2_support_scan_summary.csv": support_scan_df,
        "19_part2_frequent_itemsets.csv": frequent_itemsets_df,
        "20_part2_removed_invalid_itemsets.csv": removed_invalid_df,
        "21_part2_all_generated_rules.csv": rules_df.drop(columns=["Antecedent Itemset", "Consequent Itemset"]),
        "22_part2_surviving_rules_format_lists.csv": formats_df.drop(columns=["Consequent Predicate Count", "Consequent Attribute"]),
        "23_part3_format1_rules_treat_only.csv": format1_rules_df.drop(columns=["Consequent Predicate Count", "Consequent Attribute"]),
        "24_part3_predictions.csv": prediction_df,
        "25_part3_metrics.csv": metrics_df,
        "26_part2_balance_check.csv": balance_df,
    }

    for file_name, dataframe in outputs.items():
        dataframe.to_csv(output_dir / file_name, index=False)

    summary = {
        "raw_record_count": int(len(df)),
        "clean_record_count": int(len(clean_df)),
        "removed_record_count": int(len(df) - len(clean_df)),
        "thresholds": thresholds,
        "econ_train_size": int(len(econ_train)),
        "econ_test_size": int(len(econ_test)),
        "support_count_used": CONFIG["minimum_support_count"],
        "surviving_format1_treat_rules": int(len(format1_rules_df)),
        "metrics": metrics_df.iloc[0].to_dict(),
        "balance": balance_df.iloc[0].to_dict(),
    }
    (output_dir / "00_run_summary.json").write_text(pd.Series(summary).to_json(indent=2), encoding="utf-8")
    print(f"Run complete. Generated {len(outputs) + 1} audit files in: {output_dir}")
    print(pd.Series(summary).to_json(indent=2))


if __name__ == "__main__":
    main()
