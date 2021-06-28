# readCSVFile.py
# Type: Script
# Author: Tom Sung
# This python script reads the CSV file

# Import packages
import pandas as pd


def read_db():
    data = pd.read_csv("FoodCompatibility.csv", delimiter=',')


if __name__ == '__main__':
    read_db()
