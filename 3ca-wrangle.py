import pandas as pd
import numpy as np

# Read the Excel file into a DataFrame, skipping the first 3 rows and reading the first 15 rows
df = pd.read_excel("/Users/femisokoya/Documents/GitHub/CRA/Companies_Register_Activities_2021-22.xls",
                   sheet_name='Table_A5',
                   skiprows=3,
                   nrows=15)

# Remove columns with no values
df = df.dropna(axis=1, how='all')

# Remove rows with no values
df = df.dropna(axis=0, how='all')

# Remove numeral suffixes from column headers
df.columns = df.columns.str.replace(r'\d+$', '', regex=True)

# Update the header for column 0
df.rename(columns={df.columns[0]: 'As at 31st March 2022'}, inplace=True)

# Melt the DataFrame with 'Corporate body type' as id_vars
melted_df = pd.melt(df, id_vars=['As at 31st March 2022'], var_name='Comment', value_name='Value')

# Create a new DataFrame with the required columns
new_df = melted_df[['As at 31st March 2022', 'Comment', 'Value']].copy()

# Convert 'Value' column to floats with two decimal places
new_df['Value'] = new_df['Value'].round(2)

# Save the modified DataFrame to a CSV file
new_df.to_csv('/Users/femisokoya/Documents/GitHub/3c-cra/results.csv', index=False)

# Print the modified DataFrame to verify the changes
print(new_df.head())
