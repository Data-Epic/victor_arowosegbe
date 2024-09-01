import pandas as pd
import numpy as np 
sns.set()



# GOAL
# -Identify data sources
# -Assess data quality
# -Gain insight into structure and format of the data.
# -Identify potential challenges and opportunities in the data.


def reader(filename):
    """
    Loads in data of the specified formats
    (csv, txt, json and xlsx)

    Args:
        filename (filetype): The filename to be loaded

    Returns:
    pd.DataFrame
        A Dataframe obtained from the filetype inputed. 

    Raises:
    TypeError
        If filename is not a type of the specified filetypes.

    """
    if 'csv' not in filename:
        raise TypeError('Filename ')

    if '.csv' in filename:
        df = pd.read_csv(filename)
    elif '.txt' in filename:
        df = pd.read_fwf(filename)
    elif '.json' in filename:
        df = pd.read_json(filename)
    elif '.xlsx' in filename:
        df = pd.read_excel(filename) 
    return df


def data_preview(df):
    """
    The function gives an overview of the loaded data

    Args:
    df : pd.DataFrame
        The DataFrame to be previewed.

    Returns:
    a : A description of the number of rows and columns present in the dataframe.
    concat : a dataframe depicting the datatypes and unique values in a column.

    Raises:
    TypeError
        If df is not a pandas DataFrame


    """
    a = print('Number of rows and columns is: ', df.shape)
    data_types, unique_values  = pd.Series(df.dtypes), pd.Series(df.nunique())
    concat = pd.concat([data_types,unique_values], axis=1)
    concat = concat.rename(columns={0:'Datatypes', 1:'Unique Values'})
    return concat, a


def find_na(df):
    """
    Identifies whether the dataframe contains missing values 
    and prints a summary of the columns with its missing data number.

    Args:
    df : pd.DataFrame
        The DataFrame to search for missing values.

    Returns:
    A print statement with missing data information whether present or not.
    """
    print('\n\nFinding Missing Values')
    print(df.isna().sum())


def skewness_identifier(df, column_name = None):
    """
    A function that reviews the distribution of a column, 
    identifies skewness and uniformity if present.

    Args:
    df : pd.DataFrame
        The DataFrame to with column(s) of interest.

    column_name (list, optional): Column name with description of its parameters. Defaults to None.

    Raises:
    TypeError 
        If df is not a pandas DataFrame or column is not a list
    """
    df2 = pd.DataFrame(df.describe())
    df3 = df2.rename_axis('parameters').reset_index()

    a = df3.loc[df3['parameters'] == 'mean', column_name].tolist()
    b = df3.loc[df3['parameters'] == '50%', column_name].tolist()

    if a > b :
        print(f'Their is a possible right skewness in {column_name} column')
    
    elif a == b :
        print(f'{column_name} column has a uniform distribution')
    else:
        print(f'Their is a possible left skewness in {column_name} column')

def outlier_identifier(df, column_name = None):
    """_summary_
    A function that reviews the distribution of a column, 
    identifies outiliers.

    Args:
    df : pd.DataFrame
        The DataFrame to with column(s) of interest.

    column_name (list, optional): Column name with description of its parameters. Defaults to None.

    Raises:
    TypeError 
        If df is not a pandas DataFrame or column is not a list
    """
    df2 = pd.DataFrame(df.describe())
    df3 = df2.rename_axis('parameters').reset_index()

    median_val = df3.loc[df3['parameters'] == '50%', column_name].tolist()
    Q1 = df3.loc[df3['parameters'] == '25%', column_name].tolist()
    Q3 = df3.loc[df3['parameters'] == '75%', column_name].tolist()
    min_val = df3.loc[df3['parameters'] == 'min', column_name].tolist()
    max_val = df3.loc[df3['parameters'] == 'max', column_name].tolist()



    IQR = Q3[0] - Q1[0]

    upper_fence = Q3[0] + (1.5 * IQR)
    lower_fence = Q1[0] - (1.5 *IQR)

    if min_val[0] < lower_fence or max_val[0] > upper_fence:
        print(f'Outlier Detected in {column_name} column')
    else:
        print(f'{column_name} column does not contain an outlier')


