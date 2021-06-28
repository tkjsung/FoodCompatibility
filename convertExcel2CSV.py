# convertExcel2CSV.py
# Type: Script
# Author: Tom Sung
# Purpose: This python script contains specific variable names that converts FoodCompatibility.xlsx to a CSV file

import pandas as pd
import os.path


# Read Excel Document
def read_excel(filename):
    df = pd.read_excel(filename, sheet_name='FoodCompatibility', header=0, usecols="A:K", dtype=str)
    # print("###")
    return df


# Get rid of extra rows with N/A.
def remove_nan(df):
    counter = 0
    for x in df.item1:
        # check = df.item1[counter]
        if isinstance(x, float):  # nan is considered as float, so detect for floating instance.
            break
        counter += 1

    drop_array = list(range(counter, len(df.item1)))  # stops one value before length of df.item1
    df_update = df.drop(index=drop_array)
    df = df_update
    del df_update
    return df


# Convert to CSV. This includes checking if the file already exists.
def to_csv(df, csv_filename):
    ans = input("File is about to be converted from XLSX to CSV.\nDo you want to perform this action? (Y/N):\n")
    ans = ans.lower()
    if (ans == 'yes') or (ans == 'y'):
        logic = os.path.isfile(csv_filename)
        if logic:
            print("File exists in the writing directory. Force EOF.")
            print("File path: " + csv_filename)
            exit()
        else:
            pd.DataFrame.to_csv(df, path_or_buf=csv_filename, na_rep='N/A', index=False)
            print("File successfully converted to CSV.\nEOP")
    else:
        print("Force EOP.")
        exit()


if __name__ == '__main__':
    # File paths
    filepath = '/Users/tomsung/Desktop/FoodCompatibility.xlsx'
    csv_filepath = '/Users/tomsung/Desktop/FoodCompatibility.csv'
    # Read Excel document
    data = read_excel(filepath)
    # Remove unnecessary N/A entries
    data_noNan = remove_nan(data)
    # Convert dataframe to csv
    to_csv(data_noNan, csv_filepath)
