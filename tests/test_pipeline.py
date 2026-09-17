import math
import unittest

import pandas as pd

from data_mining_pipeline import (
    apriori_frequent_itemsets,
    calculate_metrics,
    entropy_of_labels,
    invalid_itemset_reason,
    support_count,
    validate_input_data,
)


class TestInputValidation(unittest.TestCase):
    def test_valid_input_returns_independent_attributes(self):
        frame = pd.DataFrame({"income": [1.0, 2.0], "age": [20, 30], "treat": [0, 1]})
        self.assertEqual(validate_input_data(frame), ["income", "age"])

    def test_missing_or_nonbinary_treat_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "treat"):
            validate_input_data(pd.DataFrame({"income": [1.0, 2.0]}))

        with self.assertRaisesRegex(ValueError, "only 0 and 1"):
            validate_input_data(pd.DataFrame({"income": [1.0, 2.0], "treat": [0, 2]}))


class TestCoreCalculations(unittest.TestCase):
    def test_entropy_handles_empty_pure_and_balanced_labels(self):
        self.assertEqual(entropy_of_labels([]), 0.0)
        self.assertEqual(entropy_of_labels([1, 1, 1]), 0.0)
        self.assertTrue(math.isclose(entropy_of_labels([0, 1]), 1.0))

    def test_apriori_counts_only_itemsets_meeting_support(self):
        transactions = [("A", "B"), ("A", "C"), ("A", "B")]
        levels = apriori_frequent_itemsets(transactions, min_support_count=2)

        self.assertEqual(levels[1][frozenset({"A"})], 3)
        self.assertEqual(levels[1][frozenset({"B"})], 2)
        self.assertNotIn(frozenset({"C"}), levels[1])
        self.assertEqual(levels[2][frozenset({"A", "B"})], 2)

    def test_support_and_duplicate_attribute_checks(self):
        transactions = [frozenset({"A", "B"}), frozenset({"A", "C"}), frozenset({"A", "B"})]
        self.assertEqual(support_count(transactions, frozenset({"A", "B"})), 2)

        item_to_attribute = {"A0": "age", "A1": "age", "I0": "income"}
        reason = invalid_itemset_reason(frozenset({"A0", "A1"}), item_to_attribute)
        self.assertIn("age", reason)
        self.assertEqual(invalid_itemset_reason(frozenset({"A0", "I0"}), item_to_attribute), "")

    def test_confusion_matrix_metrics(self):
        predictions = pd.DataFrame(
            {
                "Actual treat": [1, 1, 0, 0],
                "Predicted treat": [1, 0, 1, 0],
            }
        )
        metrics = calculate_metrics(predictions).iloc[0]

        self.assertEqual(metrics["TP (X)"], 1)
        self.assertEqual(metrics["FN (Y)"], 1)
        self.assertEqual(metrics["FP (Z)"], 1)
        self.assertEqual(metrics["TN (W)"], 1)
        self.assertEqual(metrics["Accuracy"], 0.5)
        self.assertEqual(metrics["Recall"], 0.5)
        self.assertEqual(metrics["Precision"], 0.5)


if __name__ == "__main__":
    unittest.main()
