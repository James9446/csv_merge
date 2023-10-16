import pandas as pd
import argparse
import os

# Create argument parser
parser = argparse.ArgumentParser(description='Combine two CSV files.')
parser.add_argument('csv1', type=str, help='Path to the first CSV file')
parser.add_argument('csv2', type=str, help='Path to the second CSV file')
parser.add_argument('--name', type=str, default='merged.csv', help='Name of the output CSV file for matched rows')
parser.add_argument('--path', type=str, default='.', help='Output directory for new CSV files')
parser.add_argument('--on', type=str, default='email', help='Column to merge on')

# Parse arguments
args = parser.parse_args()

# Load CSV files into pandas dataframes, treating all columns as strings
df1 = pd.read_csv(args.csv1, dtype=str)
df2 = pd.read_csv(args.csv2, dtype=str)

# Merge both dataframes on the specified column, keeping only those rows that have a match in both
combined = pd.merge(df1, df2, on=args.on)

# Save the combined dataframes to a new CSV file in the specified output directory
os.makedirs(args.path, exist_ok=True)
combined.to_csv(os.path.join(args.path, args.name), index=False)

# Create a filename for the unmatched CSV file, it's either 'unmatched.csv' or 'unmatched_<value of name>.csv'
unmatched_filename = 'unmatched.csv' if args.name == 'combined.csv' else 'unmatched_' + args.name

# Find rows in the specified column in df1 that are not in df2 and vice versa
df1_unmatched = df1[~df1[args.on].isin(df2[args.on])]
df2_unmatched = df2[~df2[args.on].isin(df1[args.on])]

# Combine unmatched rows from both dataframes
unmatched = pd.concat([df1_unmatched, df2_unmatched])

# Save unmatched rows to a new CSV file in the specified output directory
unmatched.to_csv(os.path.join(args.path, unmatched_filename), index=False)
