# CSV Merge

This Python script allows merging two CSV files based on a common column. By default, it considers 'email' as the common column but it can be changed according to your dataset. The script creates a new CSV file keeping all columns from both CSVs. If any rows do not find a matching value in the other CSV based on the common column, those rows are added to a separate CSV file.

## Features

- Merges two CSV files based on a common column.
- Outputs two CSVs: one for rows with matching values and the other for rows without a match.
- The common column can be specified while running the script (defaults to 'email').

## Requirements

Python 3.x and Pandas library are required.

### Installation

Make sure you have Python3 and pip (Python package installer) installed on your system. Then use pip to install pandas:

```bash
pip install pandas
```
- If you have both Python2 and Python3 installed and Python3 is not your default Python version, you may have to use `pip3 install pandas` to install for Python3. 

- If you only have Python3 installed or it's your default version, `pip install pandas` should work fine. 

If you're not sure, you can always use `python3 -m pip install pandas` which will definitely install pandas for Python3.

## Usage 

To run the script, use the following command structure:

```bash
python csv_merge.py csv1 csv2 --name outputfile --path outputdirectory --on column
```

Where:

- `csv1` : Path to the first CSV file. (required)
- `csv2` : Path to the second CSV file. (required)
- `--name` : Name of the output file for matched rows. Defaults to 'combined.csv'. (optional)
- `--path` : Directory to save the output files. Defaults to the current directory. (optional)
- `--on` : Column to merge on. Defaults to 'email'. (optional)

If the `--name` argument is included then the unmatched CSV file name will be a concatention of `'unmatched_' + name`. If the `--name` argument is not included then the unmatched CSV file name will be `unmatched.csv`

### Example:

```bash
python csv_merge.py data1.csv data2.csv --name result.csv --path /home/user/Results/ --on customerId
```

In the above example, the script will:
- Merge 'data1.csv' and 'data2.csv' based on the 'customerId' column.
- Write the merged data to '/home/user/Results/result.csv'.
- Rows in either data1.csv or data2.csv that do not have a matching 'customerId' in the other file will be written to '/home/user/Results/unmatched_result.csv'.
- If every row has a match, an unmatched CSV will still be created. It will just only have the header columns. 

Enjoy merging your CSV files with ease!