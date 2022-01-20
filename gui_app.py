# gui_app.py
# Type: Script
# Author: Tom Sung
# Purpose: GUI App Functionality for FoodCompatibility is written here.

# Import relevant libraries
import tkinter as tk
import foodSearch


# Global variable required for foodSearch.py
lang = ''
searchTerm = ''
entryList = []
text_out_str = []


# This should be written as a class and __init__, but I don't want to figure it out right now.
def gui():
    ############ Window Size ############
    win_width = 800
    win_height = 530
    win_xpos = 200
    win_ypos = 100
    win_width_min = 500
    win_height_min = 380

    ############ Create window ############
    root = tk.Tk()
    root.title("Food Compatibility Search Tool")
    root.geometry(f"{win_width}x{win_height}+{win_xpos}+{win_ypos}")  # (width x height + XPOS + YPOS on monitor)
    root.configure(background="#51C9ED")
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.minsize(width=win_width_min, height=win_height_min) # Limit window size. Will not go smaller than this.

    ############ Create frames needed for this app ############
    frame_main = tk.Frame(master=root); frame_main.configure(background="#51C9ED")
    frame_topBanner = tk.Frame(master=frame_main); frame_topBanner.configure(background="#51C9ED")
    frame_dropdown = tk.Frame(master=frame_topBanner, pady=2); frame_dropdown.configure(background="#51C9ED")
    frame_search = tk.Frame(master=frame_main, borderwidth=2, pady=5); frame_search.configure(background="#51C9ED")
    frame_warning = tk.Frame(master=frame_main, borderwidth=0.5, pady=1); frame_warning.configure(background="#51C9ED")
    frame_outText = tk.Frame(master=frame_main, borderwidth=2, pady=5); frame_outText.configure(background="#51C9ED")

    ############ TOP BANNER ELEMENTS: Title Text and Language Selector (frame_topBanner) ############
    # TOP BANNER 1: Title Text
    label_title = tk.Label(master=frame_topBanner, text="Food Compatibility Search Tool")
    label_title.config(font=("Helvetica", 24)); label_title.configure(background="#51C9ED")
    label_title.pack(side=tk.TOP)

    # frame_main.grid_rowconfigure(0, weight=1)
    # frame_main.grid_columnconfigure(0, weight=1)

    # TOP BANNER 2: Dropdown Language Selector (frame_dropdown)
    label_lang = tk.Label(master=frame_dropdown, text="Search Language: ")
    label_lang.configure(background="#51C9ED")
    label_lang.grid(row=0, column=1)
    optionsList_lang = ['English (EN)', 'Traditional Chinese (ZH)']
    var_lang = tk.StringVar(master=frame_dropdown)
    var_lang.set(optionsList_lang[0])
    option_lang = tk.OptionMenu(frame_dropdown, var_lang, *optionsList_lang)
    option_lang.grid(row=0, column=2, sticky='e')

    ''' # In the future, maybe search by entry number ############
    label_searchType = tk.Label(master=frame_dropdown, text="Search Type: ")
    label_searchType.grid(row=1, column=0)
    optionsList_searchType = ['Search by Term', 'Search by Entry No.']
    var_searchType = tk.StringVar(master=frame_dropdown)
    var_searchType.set(optionsList_searchType[0])
    option_searchType = tk.OptionMenu(frame_dropdown, var_searchType, *optionsList_searchType)
    option_searchType.grid(row=1, column=1, sticky='e')
    '''

    frame_dropdown.pack()
    # frame_dropdown.grid(row=0, column=1, sticky='ne')
    frame_topBanner.pack(side=tk.TOP, anchor='center', fill='both')

    ############ SEARCH BAR ELEMENTS (frame_search) ############
    label_search = tk.Label(master=frame_search, text="Search Text: ")
    label_search.grid(row=0, column=0)
    label_search.configure(background="#51C9ED")
    entry_search = tk.Entry(master=frame_search)
    entry_search.grid(row=0, column=1)
    entry_search.focus_set()

    # On button press, edit the text in the result box.
    def on_button():
        global lang, searchTerm, text_out_str
        searchTerm = entry_search.get()
        searchLang = var_lang.get()
        if searchLang in optionsList_lang[0]:
            lang = 'en'
        else:
            lang = 'zh'
        foodSearch_algo()
        text_out.config(state=tk.NORMAL)
        text_out.delete("1.0", tk.END)
        for x in range(0, len(text_out_str)):
            text_out.insert(tk.INSERT, text_out_str[x] + "\n")
        # text_out.insert(tk.INSERT, "TEST123\n")
        text_out.config(state=tk.DISABLED)
        text_out_str = []

    button = tk.Button(master=frame_search, text="Search", command=on_button)
    button.grid(row=0, column=2)
    frame_search.pack(side="top")

    label_warning = tk.Label(master=frame_warning, text="使用中文時，請在另應用程式填寫文字，然後再複製及貼上在上面的輸入框")
    label_warning.configure(background="#51C9ED")
    label_warning.pack(side=tk.TOP)
    frame_warning.pack(side=tk.TOP)

    ############ OUTPUT RESULT BOX (frame_outText) ############
    scroll_outText = tk.Scrollbar(master=frame_outText)
    scroll_outText.pack(side=tk.RIGHT, fill=tk.Y)  # Adding scrollbar to the text widget (vertical, right side)

    text_out = tk.Text(master=frame_outText, wrap=tk.WORD, yscrollcommand=scroll_outText.set, height=19) # height means lines of text
    text_out.config(font=("Helvetica", 14)); text_out.configure(background="#51C9ED")
    # text_out.tag_configure("tag_name", justify='center')
    text_out.insert(tk.INSERT, "### Please enter search term in the box above. ###\n")
    text_out.config(state=tk.DISABLED)  # This disables the text editing function inside the text box
    # text_out.tag_configure("tag_name", justify='left')
    # text_out.pack(expand='yes', fill='both')
    text_out.pack(expand=1, fill=tk.X)

    scroll_outText.config(command=text_out.yview)  # Scrollbar will scroll through the text widget vertically
    frame_outText.pack(side='top', fill=tk.X, expand=1, padx=10, pady=10)

    label_credit = tk.Label(master=frame_main)
    label_credit.configure(background="#51C9ED")
    label_credit.config(text="Copyright \u00a9 2021 Tom (Ke-Jun) Sung. All rights reserved.")
    label_credit.pack()

    ############ Packing the main frame ############
    frame_main.pack(side='top', fill='both', expand='yes', padx=10, pady=10)
    # frame_main.grid(padx=10, pady=10, sticky='nswe')

    ############ Run the window/app ############
    root.mainloop()


def foodSearch_algo():
    global entryList
    ############ SEARCH: Find index of the search term. Note that this is written due to repetitiveness ############
    def find_index(temp_list):
        for x in temp_list:
            if isinstance(x[1], float):
                continue
            elif searchTerm in x[1]:
                temp = x[0]
                entryList.append(temp)

    if lang == "en":
        tempList = list(enumerate(df.item1_EN)); find_index(tempList)
        tempList = list(enumerate(df.item2_EN)); find_index(tempList)
        tempList = list(enumerate(df.item3plus_EN)); find_index(tempList)
    else:
        tempList = list(enumerate(df.item1)); find_index(tempList)
        tempList = list(enumerate(df.item2)); find_index(tempList)
        tempList = list(enumerate(df.item3plus)); find_index(tempList)

    ############ Check for duplicates ############
    entryList = list(set(entryList))  # set() gets unique set of items
    entryList.sort()

    ############ Display Results ############
    # For GUI, put everything in a string.
    global text_out_str
    if len(entryList) == 0:
        text_out_str.append("### No search results for \"" + searchTerm + "\". ###")
    elif len(searchTerm) == 0:
        text_out_str.append("### The search box is empty. Please input a search item. ###")
    else:
        # print("Search Results for " + foodTerm + ":")
        for num in entryList:
            if lang == "en":
                food1 = df.item1_EN[num]
                food2 = df.item2_EN[num]
                food3 = df.item3plus_EN[num]
            else:
                food1 = df.item1[num]
                food2 = df.item2[num]
                food3 = df.item3plus[num]
            compat = str(df.compatibility[num])
            compat = compat.capitalize()
            if isinstance(food3, float):
                del food3  # This means food3 is N/A. Remove entry from displaying
                text_out_str.append("[" + compat + "] Entry #" + str(num + 1) + ": " + food1 + " & " + food2)
                # print("[" + compat + "] Entry #" + str(num + 1) + ": " + food1 + " & " + food2)
            else:
                text_out_str.append("[" + compat + "] Entry #" + str(num + 1) + ": " + food1 + ", " + food2 +
                                    " & " + food3)
                # print("[" + compat + "] Entry #" + str(num + 1) + ": " + food1 + ", " + food2 + " & " + food3)
        text_out_str.append("\n### END OF LIST ###")
    entryList = []

if __name__ == '__main__':
    df = foodSearch.read_db()
    gui()
