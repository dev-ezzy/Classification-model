import pandas as pd
from IPython import display

import pandas as pd

import pandas as pd

def data_summary(file_name):
    # Read the CSV file into a DataFrame
    file_path = f'./{file_name}'  # Assuming the file is in the same directory as the script
    df = pd.read_csv(file_path)

    # Show the first 5 rows of the DataFrame
    print("First 5 rows of the DataFrame:")
    print(df.head())  # Use df.head() to display the DataFrame

    # Display summary information about the DataFrame
    print("\nDataFrame Info:")
    print(df.info())  # Use print to display DataFrame info

    # Show summary statistics of the DataFrame
    print("\nSummary Statistics:")
    print(df.describe())  # Use print to display DataFrame statistics

# Call the function with the file name as an argument
 # Replace 'your_file.csv' with the actual file name


# def data_summary(file_name):
#     # Read the CSV file into a DataFrame
#     file_path = f'./{file_name}'  # Assuming the file is in the same directory as the script
#     display.df = pd.read_csv(file_path)

#     # Show the first 5 rows of the DataFrame
#     print("First 5 rows of the DataFrame:")
#     display.df.head

#     # Display summary information about the DataFrame
#     print("\nDataFrame Info:")
#     display.df.info()

#     # Show summary statistics of the DataFrame
#     print("\nSummary Statistics:")
#     display.df.describe()


# print("""
#     Dropping "waterpoint_type" because it has similar values to "waterpoint_type_group" and has misssing values.
#     The percentage of missing data data is also very insignificant when we compare with the amount of data we have. 
#     Imputting these missing values with the mean or median for numeric
#     values and mode for categorical columns may add weight on certain features and this might affect our model
#     when making predictions.Dropping these values is the best solution.""")


