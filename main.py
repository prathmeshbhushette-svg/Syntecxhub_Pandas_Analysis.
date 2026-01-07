Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import pandas as pd
... 
... # Load the file
... df = pd.read_csv('your_data.csv')
... 
... # Inspect the data
... print(df.head())     # Shows first 5 rows
... print(df.info())     # Shows data types and missing values
... [9:38 am, 07/01/2026] prathmeshbhushette: # Basic math on your columns
... print(df.describe()) # Shows mean, median, min, max for all numbers
... [9:38 am, 07/01/2026] prathmeshbhushette: # Example: Filter rows where a column value is greater than 50
... filtered_df = df[df['your_column_name'] > 50]
... 
... # Save the result
