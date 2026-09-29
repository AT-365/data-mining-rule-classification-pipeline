import json
import py_compile
import unittest
import zipfile
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
ASSIGNMENT_1 = REPOSITORY_ROOT / "assignment1_package"
ASSIGNMENT_2 = REPOSITORY_ROOT / "assignment2_package"


class PortfolioChecks(unittest.TestCase):
    def test_expected_project_structure_exists(self):
        expected_paths = [
            REPOSITORY_ROOT / "README.md",
            ASSIGNMENT_1 / "README.md",
            ASSIGNMENT_1 / "data" / "Assignment-1-Data.csv",
            ASSIGNMENT_1 / "outputs" / "00_run_summary.json",
            ASSIGNMENT_2 / "README.md",
            ASSIGNMENT_2 / "data",
            ASSIGNMENT_2 / "outputs" / "id3" / "00_run_summary.json",
            ASSIGNMENT_2 / "outputs" / "bayes" / "00_run_summary.json",
        ]
        for path in expected_paths:
            with self.subTest(path=path):
                self.assertTrue(path.exists())

    def test_python_files_compile_without_truncation(self):
        python_files = [
            ASSIGNMENT_1 / "DataMining_Assignment1Pipeline_v1_20260402_FullSubmission.py",
            ASSIGNMENT_2 / "DataMining_Assignment2Pipeline_v1_20260506_FullSubmission.py",
        ]
        for path in python_files:
            with self.subTest(path=path):
                py_compile.compile(path, doraise=True)

    def test_no_merge_conflict_markers_remain(self):
        markers = ("<" * 7, "=" * 7, ">" * 7)
        extensions = {".md", ".py", ".txt", ".json", ".csv", ".yml", ".yaml"}
        for path in REPOSITORY_ROOT.rglob("*"):
            if path.is_file() and path.suffix.lower() in extensions and ".git" not in path.parts:
                text = path.read_text(encoding="utf-8", errors="replace")
                with self.subTest(path=path):
                    self.assertFalse(any(marker in text for marker in markers))

    def test_assignment_1_verified_metrics(self):
        summary_path = ASSIGNMENT_1 / "outputs" / "00_run_summary.json"
        summary = json.loads(summary_path.read_text(encoding="utf-8"))
        self.assertEqual(summary["raw_record_count"], 414)
        self.assertEqual(summary["clean_record_count"], 309)
        self.assertEqual(summary["econ_train_size"], 277)
        self.assertEqual(summary["econ_test_size"], 32)
        self.assertAlmostEqual(summary["metrics"]["Accuracy"], 0.5625)

    def test_assignment_1_output_count(self):
        output_files = list((ASSIGNMENT_1 / "outputs").glob("*"))
        self.assertEqual(len(output_files), 27)

    def test_assignment_2_verified_metrics(self):
        id3 = json.loads(
            (ASSIGNMENT_2 / "outputs" / "id3" / "00_run_summary.json").read_text(encoding="utf-8")
        )
        bayes = json.loads(
            (ASSIGNMENT_2 / "outputs" / "bayes" / "00_run_summary.json").read_text(encoding="utf-8")
        )
        self.assertAlmostEqual(id3["Final Accuracy Percent"], 47.7272727273)
        self.assertEqual(id3["T1 Threshold"], 0.8)
        self.assertEqual(id3["g Parameter"], 0.01)
        self.assertAlmostEqual(bayes["Final Accuracy Percent"], 45.4545454545)
        self.assertEqual(bayes["Smoothing Used"], "Yes")

    def test_assignment_2_office_files_are_valid(self):
        office_files = list(ASSIGNMENT_2.rglob("*.xlsx")) + list(ASSIGNMENT_2.rglob("*.docx"))
        self.assertGreater(len(office_files), 0)
        for path in office_files:
            with self.subTest(path=path):
                self.assertTrue(zipfile.is_zipfile(path))

    def test_assignment_2_expected_workbook_counts(self):
        id3_workbooks = list((ASSIGNMENT_2 / "outputs" / "id3").glob("*.xlsx"))
        bayes_workbooks = list((ASSIGNMENT_2 / "outputs" / "bayes").glob("*.xlsx"))
        self.assertEqual(len(id3_workbooks), 20)
        self.assertEqual(len(bayes_workbooks), 17)


if __name__ == "__main__":
    unittest.main()
