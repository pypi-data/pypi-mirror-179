import csv
from pandas import read_csv, errors


def read_txt(filepath_or_buffer, column_names, max_rows_to_try: int = None, separator: str = ",", encode: str = "utf-8",
             is_commented: bool = False):
    """column_name can be a string, a list of strings, a tuple of strings, or a set of strings."""

    def print_comment(comment: str):
        if is_commented:
            print(comment)

    # 1. If column_names is not a string, list, tuple, or set, raise TypeError
    if not isinstance(column_names, str) and not isinstance(column_names, list) \
            and not isinstance(column_names, tuple) and not isinstance(column_names, set):
        raise TypeError("column_names has to be a list, tuple, or string")

    # 2. Open the text file to determine the number of rows to try
    with open(filepath_or_buffer, 'r', encoding=encode) as f:
        reader = csv.reader(f)
        num_rows = len(list(reader))
    if max_rows_to_try is None or max_rows_to_try > num_rows:
        max_rows_to_try = num_rows

    # 3. Try to read the text row by row until it seems to work
    # There is no guarantee that whatever df pandas can read is your intended df, but I hope this works in most cases
    print_comment(f"\n* Read {filepath_or_buffer}")
    for i in range(0, max_rows_to_try):
        # Try to read the text file as df
        try:
            df = read_csv(filepath_or_buffer, sep=separator, encoding=encode, skiprows=i)
            # Check if any column name in df matches column_names as a string
            if isinstance(column_names, str) and column_names in df.columns:
                print_comment(f"* Found {len(df.columns)} columns: {[x for x in df.columns]}")
                return df
            elif (isinstance(column_names, list) or isinstance(column_names, tuple)) \
                    and all(x in df.columns for x in column_names):
                print_comment(f"* Found {len(df.columns)} columns: {[x for x in df.columns]}")
                return df
            elif isinstance(column_names, set) and column_names.issubset(df.columns):
                print_comment(f"* Found {len(df.columns)} columns: {[x for x in df.columns]}")
                return df
            else:
                continue
        # If the pandas.errors.ParserError occurs, print the row number and skip to the next row
        except errors.ParserError:
            print_comment(f"* pandas.errors.ParserError at row {i+1}. Trying the next row...")
            pass
