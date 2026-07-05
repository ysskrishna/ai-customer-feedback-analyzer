import unittest

from core.csv_feedback import find_feedback_column, parse_feedback_csv


class CsvFeedbackTest(unittest.TestCase):
    def test_find_feedback_column_accepts_xquik_text_alias(self) -> None:
        self.assertEqual(
            find_feedback_column(["text", "createdAt"]),
            "text",
        )

    def test_parse_feedback_csv_filters_blank_rows(self) -> None:
        rows, detected_column = parse_feedback_csv(
            b"Customer Feedback,createdAt\n Great support ,2026-01-01\n ,2026-01-02\n",
        )
        self.assertEqual(detected_column, "Customer Feedback")
        self.assertEqual(rows, ["Great support"])

    def test_parse_feedback_csv_rejects_missing_feedback_column(self) -> None:
        with self.assertRaisesRegex(ValueError, "feedback column"):
            parse_feedback_csv(b"rating\n5\n")


if __name__ == "__main__":
    unittest.main()
