# foodSearch.py
# Type: Script
# Author: Tom Sung
# Purpose: This script contains all the functions needed to enable search functionality for the Food Compatibility
#          app.

# Import packages
import pandas as pd


# Global variables
lang = ""
foodTerm = ""
entry_list = []


# 1. Read database (from CSV file)
def read_db():
    # Make sure FoodCompatibility.csv is in the same folder as this script (makes life easier)
    data = pd.read_csv("FoodCompatibility.csv", delimiter=',')
    return data


# 2. Get Input and Check
def get_input():
    global foodTerm
    get_lang()  # Using another function since this requires checks.
    foodTerm = input("What food item do you want to check?: ")
    if lang == "en":
        foodTerm = foodTerm.lower()
    return lang, foodTerm


# 2a. Check Language Settings
def get_lang():
    global lang
    logic = 0
    while logic == 0:
        lang = input("Language? (ZH/EN): ")
        lang = lang.lower()
        if ("zh" in lang) or ("en" in lang):
            logic = 1
        else:
            print("Language not supported or Incorrect Input. Try again.")


# 3. Actual Search
def search(data):
    # Find the index of the search term. Note that this function is written due to repetitiveness.
    def find_index(tempList):
        for x in tempList:
            if isinstance(x[1], float):
                continue
            elif foodTerm in x[1]:
                temp = x[0] + 1
                entry_list.append(temp)

    tempList = list(enumerate(data.item1_EN)); find_index(tempList)
    tempList = list(enumerate(data.item2_EN)); find_index(tempList)
    tempList = list(enumerate(data.item3plus_EN)); find_index(tempList)


# 4. Check for duplicates in the entry_list list
# TODO: remove entries if duplicates are found. Note that the duplicates will both show up as positive
#       in other words, if "1" is repeated, then both "1"s will be marked as repeated. Figure out a way to circumvent
#       this issue.
def check_duplicate():
    for x in entry_list:
        if entry_list.count(x) > 1:
            print("Repeated entry")
        else:
            print("Not repeated.")


if __name__ == '__main__':
    df = read_db()
    # out = get_input()
    lang = "en"; foodTerm = "broccoli"
    search(df)
    check_duplicate()
    print(entry_list)
    print("Test123")

