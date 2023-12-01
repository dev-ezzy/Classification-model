import pandas as pd
from IPython import display

import pandas as pd

import pandas as pd

# def data_summary(file_name):
#     # Read the CSV file into a DataFrame
#     file_path = f'./{file_name}'  # Assuming the file is in the same directory as the script
#     df = pd.read_csv(file_path)

#     # Show the first 5 rows of the DataFrame
#     print("First 5 rows of the DataFrame:")
#     print(df.head())  # Use df.head() to display the DataFrame

#     # Display summary information about the DataFrame
#     print("\nDataFrame Info:")
#     print(df.info())  # Use print to display DataFrame info

#     # Show summary statistics of the DataFrame
#     print("\nSummary Statistics:")
#     print(df.describe())  # Use print to display DataFrame statistics
#     return df

# import pandas as pd

# def data_summary(file_name):
#     # Read the CSV file into a DataFrame
#     file_path = f'./{file_name}'  # Assuming the file is in the same directory as the script
#     df = pd.read_csv(file_path)

#     # Show the first 5 rows of the DataFrame
#     print("First 5 rows of the DataFrame:")
#     print(df.head())  # Use print to display the DataFrame

#     # Display summary information about the DataFrame
#     print("\nDataFrame Info:")
#     print(df.info())  # Use print to display DataFrame info

#     # Show summary statistics of the DataFrame
#     print("\nSummary Statistics:")
#     print(df.describe())  # Use print to display DataFrame statistics

#     return df  # Return the DataFrame for further use


# import pandas as pd

# def data_summary(file_name):
#     # Read the CSV file into a DataFrame
#     file_path = f'./{file_name}'  # Assuming the file is in the same directory as the script
#     df = pd.read_csv(file_path)

#     summary_data = []

#     # Iterate through each column
#     for column in df.columns:
#         unique_values_count = df[column].nunique()
#         sample_values = df[column].unique()[:5]  # Displaying the first 5 unique values
#         missing_values_count = df[column].isnull().sum()

#         summary_data.append({
#             'Feature Name': column,
#             'Number of Unique Values': unique_values_count,
#             'Unique Values': list(sample_values),
#             'Missing Values': missing_values_count
#         })

#     # Create a DataFrame from the summary data
#     summary_df = pd.DataFrame(summary_data)

#     return summary_df

# # Usage example:

import pandas as pd

def data_summary(file_name):
    # Read the CSV file into a DataFrame
    file_path = f'./{file_name}'  # Assuming the file is in the same directory as the script
    df = pd.read_csv(file_path)

    # Get the first 5 rows of the DataFrame
    first_5_rows = df.head(5)

    # Get summary information
    info_summary = df.info()
    describe_summary = df.describe()

    # Create DataFrames for info and describe summaries
    info_df = pd.DataFrame({'Info': [info_summary]})
    describe_df = pd.DataFrame({'Describe': [describe_summary]})
    return df, describe_summary,describe_df

    # Combine all summaries into a single DataFrame
    # summary_df = pd.concat([first_5_rows, info_df, describe_df], axis=0)

    # return summary_df

# Usage example:
# summary_dataframe = data_summary('your_file.csv')


# Usage example:


