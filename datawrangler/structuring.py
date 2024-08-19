import pandas as pd
import numpy as np 

import discover as dis
# GOAL
# Structure (Organize and format raw data to facilitate efficient analysis. Depends on analytical model to be used.)
# -Reshaping data
# -Handling missing values
# -Converting data types
# Lays the groundwork for further manipulation & exploration.


# Searching - Searching entails locating a certain piece inside a specified data structure. When the needed ingredient is discovered, it is termed a success. Searching is an operation that may be done on data structures such as arrays, linked lists, trees, graphs, and so on.
# Sorting - Sorting is the process of ordering all data elements in a data structure in a certain order, such as ascending or descending order.
# Insertion entails adding new data items to the data structure.
# The data elements in the data structure can be deleted.
# Updating - We can update or replace existing data structure parts.
# https://www.simplilearn.com/tutorials/data-structure-tutorial/what-is-data-structure


# STEPS
# Step 1: Reshaping data
# Step 2: Handling missing values
# Step 3: Datatypes conversion.
# Step 4: Data insertion & deletion.

def reshape(data, method= 'stack'):

    method_list = ['stack', 'unstack', 'melt', 'pivot']

    for method in method_list:
        if method == 'stack':
            data_reshape = data.stack()
        elif method == 'unstack':
            data_reshape = data.unstack()
    return data_reshape


def handle_missing_data(data):
    missing_data_info = data.isna().sum()

    pass

def dtype_conversion():
    pass

def data_insertion():
    pass

def data_deletion():
    pass


file = "user_journey_raw.csv"
a = dis.reader(filename=file)
print(a)

b = dis.data_preview(a)
print(b)

print(reshape(a, method='unstack'))
# print(reshape(c))
