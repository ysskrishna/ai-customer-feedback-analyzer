import csv
from io import StringIO


FEEDBACK_COLUMN_ALIASES = (
    "feedback",
    "customer_feedback",
    "text",
    "review",
    "comment",
    "comments",
    "message",
)


def normalize_column_name(column_name: str) -> str:
    return column_name.strip().lower().replace(" ", "_").replace("-", "_")


def find_feedback_column(fieldnames):
    normalized_columns = [normalize_column_name(fieldname) for fieldname in fieldnames]
    for alias in FEEDBACK_COLUMN_ALIASES:
        if alias in normalized_columns:
            return fieldnames[normalized_columns.index(alias)]
    return None


def parse_feedback_csv(csv_bytes):
    csv_text = csv_bytes.decode("utf-8-sig")
    reader = csv.DictReader(StringIO(csv_text))
    if reader.fieldnames is None:
        raise ValueError("The CSV file must include a header row.")

    feedback_column = find_feedback_column(reader.fieldnames)
    if feedback_column is None:
        aliases = ", ".join(FEEDBACK_COLUMN_ALIASES)
        raise ValueError(f"The CSV must contain one feedback column: {aliases}.")

    feedback_rows = []
    for row in reader:
        feedback_text = str(row.get(feedback_column) or "").strip()
        if feedback_text:
            feedback_rows.append(feedback_text)

    if not feedback_rows:
        raise ValueError("The feedback column does not contain any valid text.")

    return feedback_rows, feedback_column
