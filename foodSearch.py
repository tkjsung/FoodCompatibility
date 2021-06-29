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
    # 3a. Find the index of the search term. Note that this function is written due to repetitiveness.
    def find_index(temp_list):
        for x in temp_list:
            if isinstance(x[1], float):
                continue
            elif foodTerm in x[1]:
                temp = x[0]
                entry_list.append(temp)
    if lang == "en":
        tempList = list(enumerate(data.item1_EN)); find_index(tempList)
        tempList = list(enumerate(data.item2_EN)); find_index(tempList)
        tempList = list(enumerate(data.item3plus_EN)); find_index(tempList)
    else:
        tempList = list(enumerate(data.item1)); find_index(tempList)
        tempList = list(enumerate(data.item2)); find_index(tempList)
        tempList = list(enumerate(data.item3plus)); find_index(tempList)


# 4. Check for duplicates in the entry_list list
def check_duplicate():
    # for x in entry_list:
    #     if entry_list.count(x) > 1:  # If the same element is detected more than once
    #         print("Repeated entry")
    #     else:
    #         print("Not repeated.")
    global entry_list
    entry_list = list(set(entry_list))
    entry_list.sort()


# 5. Display results
# Could be changed in the future if item3plus contains more than 3 items
def display_results(data):
    if len(entry_list) == 0:
        print("No search results for " + foodTerm + ".")
    else:
        print("Search Results for " + foodTerm + ":")
        for num in entry_list:
            if lang == "en":
                food1 = data.item1_EN[num]
                food2 = data.item2_EN[num]
                food3 = data.item3plus_EN[num]
            else:
                food1 = data.item1[num]
                food2 = data.item2[num]
                food3 = data.item3plus[num]
            compat = str(data.compatibility[num])
            compat = compat.capitalize()
            if isinstance(food3, float):
                del food3
                print("[" + compat + "] Entry #" + str(num + 1) + ": " + food1 + " & " + food2)
            else:
                print("[" + compat + "] Entry #" + str(num + 1) + ": " + food1 + ", " + food2 + " & " + food3)


if __name__ == '__main__':
    df = read_db()  # Read database file
    # out = get_input()  # Get search term from user

    # lang = "en"; foodTerm = "shrimp"
    lang = "zh"; foodTerm = "蝦"

    search(df)  # Search the term given by user

    # entry_list = [10, 43, 1, 5, 2, 3, 1, 5, 6, 10, 9, 1]
    # print("orig list: " + str(entry_list))

    check_duplicate()  # Check if the search results contain any duplicates
    display_results(df)  # Display search results

    # print("new list: " + str(entry_list))
    print("#### EOP ####")

