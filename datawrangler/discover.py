import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()



# GOAL
# -Identify data sources
# -Assess data quality
# -Gain insight into structure and format of the data.
# -Identify potential challenges and opportunities in the data.


# STEPS
# Step 1: Importing library. import pandas as pd.
# Step 2: Reading data....
# Step 3: Understanding the data types, number of rows and columns....
# Step 4: Observing categorical data....
# Step 5: Exploring data....
# Step 6: Finding the missing values....
# Step 7: Visualising data.
#https://www.kdnuggets.com/2020/03/python-pandas-data-discovery.html

def reader(filename):
    """_summary_

    Args:
        filename (_type_): _description_

    Returns:
        _type_: _description_
    """
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
    """_summary_

    Args:
        df (_type_): _description_
    """
    print('Number of rows and columns is: ', df.shape)
    data_types, unique_values  = pd.Series(df.dtypes), pd.Series(df.nunique())
    concat = pd.concat([data_types,unique_values], axis=1)
    concat = concat.rename(columns={0:'Datatypes', 1:'Unique Values'})
    return concat


def find_na(df):
    """_summary_

    Args:
        df (_type_): _description_
    """
    print('\n\nFinding Missing Values')
    print(df.isna().sum())

def visualize_df(data, x_axis = None,  y_axis = None, height = None, chart = 'bar'):
    # attributes
    # -dataframe [dataset]
    # -data category [qualitative, quantitative & hybrid]
    # -chart type [will depend on data category]
    # -column name(s)
    """_summary_

    Args:
        data (dataframe): dataset to be explored visually.
        x (series-column, optional): _description_. Defaults to None.
        y (series-column, optional): _description_. Defaults to None.
        height (series-column, optional): _description_. Defaults to None.
        chart (str-chart type, optional): _description_. Defaults to 'bar'.
    """
    
    chart_type = ['bar', 'line', 'sac', 'histogram', 'scatter plot']
    for chart in chart_type:
        if chart == 'bar':
            plt.bar(x= data[x_axis], height= data[height])
        elif chart == 'line':
            plt.plot(x= data[x_axis], y=  data[y_axis])
        elif chart == 'histogram':
            plt.hist(x =data[x_axis])
            print(plt.show())
        elif chart == 'scatter plot':
            plt.scatter(x=data.loc[x_axis], y= data.loc[y_axis])
    return plt.show()


if __name__ == '__main__':
    main()


# file = "user_journey_raw.csv"
# a = reader(filename=file)
# # print(a)

# b = data_preview(a)
# print(b)

# # print(find_na(a))


# print(visualize_df(data = a, x_axis='subscription_type', height='user_id', chart='bar'))


