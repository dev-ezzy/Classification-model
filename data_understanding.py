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
    display.df.head()  # Use df.head() to display the DataFrame

    # Display summary information about the DataFrame
    print("\nDataFrame Info:")
    display.df.info()  # Use print to display DataFrame info

    # Show summary statistics of the DataFrame
    print("\nSummary Statistics:")
    display.df.describe()  # Use print to display DataFrame statistics



