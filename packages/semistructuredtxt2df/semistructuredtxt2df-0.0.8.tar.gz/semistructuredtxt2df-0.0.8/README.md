# semistructuredtxt2df

This Python package reads a text file with unknown rows of headers (e.g., when skiprows can vary) and returns a pandas DataFrame object.
With this package, you can "skip first couple of lines while reading lines in Python" (https://stackoverflow.com/questions/9578580/skip-first-couple-of-lines-while-reading-lines-in-python-file).


## License

![GitHub](https://img.shields.io/github/license/iiokentaro/semistructuredtxt2df)


## Installation

Install my-project with npm

```bash
pip install semistructuredtxt2df
```
    
## Usage/Examples
For example, this package can read this sample file as a pandas DataFrame by skipping headers that can vary.

### Arguments, data types, and default values if any
* filepath_or_buffer: str
* column_names: str, list, tuple, or set
  * The first row in the text file that contains all of the elements in it is recognized as the dataframe column names, so you do not have to specify all the columns unless you want to. The order of the column names does not matter.
* max_rows_to_try: int = None
* separator: str = ","
* encode: str = "utf-8"
* is_commented: bool = False

### Sample file (sample_data/sample_text_file.csv)

```text
"Game Is FIFA World Cup"
"Year Is 2022"
"Group Is E"
"Timestamp: 1669866143"

"This is a random comment."
"This is also a random comment."
"Country, is also included in this row, but this row will be skipped."

"Country","MP","W","D","L","GF","GA","GD","Pts"
"Spain",1,1,1,0,8,1,7,4
"Japan",2,1,0,1,2,2,0,3
"Costa Rica",2,1,0,1,1,7,-6,3
"Germany",2,0,1,1,2,3,-1,1
```
### Sample code
```python
# Import the package
from semistructuredtxt2df import read_txt

# Try reading sample files with different column_names
df1 = read_txt(r"sample_text_file.csv", "Country")
df2 = read_txt(r"sample_text_file.csv", ["Country"])
df3 = read_txt(r"sample_text_file.csv", ["Country", "Pts"])

# Check if df1, df2, and df3 are the same
print(df1.equals(df2))
print(df1.equals(df3))

print(df1)
```
### Output
```text
True
True
      Country  MP  W  D  L  GF  GA  GD  Pts
0       Spain   1  1  1  0   8   1   7    4
1       Japan   2  1  0  1   2   2   0    3
2  Costa Rica   2  1  0  1   1   7  -6    3
3     Germany   2  0  1  1   2   3  -1    1

Process finished with exit code 0
```
