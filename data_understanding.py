import pandas as pdpip

import pandas as pd

def data_summary(file_name):
    # Read the CSV file into a DataFrame
    file_path = f'./{file_name}'  # Assuming the file is in the same directory as the script
    df = pd.read_csv(file_path)

    # Show the first 5 rows of the DataFrame
    print("First 5 rows of the DataFrame:")
    df.head

    # Display summary information about the DataFrame
    print("\nDataFrame Info:")
    df.info()

    # Show summary statistics of the DataFrame
    print("\nSummary Statistics:")
    df.describe()


print("""
    Dropping "waterpoint_type" because it has similar values to "waterpoint_type_group" and has misssing values.
    The percentage of missing data data is also very insignificant when we compare with the amount of data we have. 
    Imputting these missing values with the mean or median for numeric
    values and mode for categorical columns may add weight on certain features and this might affect our model
    when making predictions.Dropping these values is the best solution.""")