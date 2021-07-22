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


# This should be written as a class and __init__, but I don't want to figure it out right now.
def gui():
    # Window Size ############
    win_width = 900
    win_height = 700
    win_xpos = 200
    win_ypos = 100

    # Create window ############
    root = tk.Tk()
    root.title("Food Compatibility Search Tool")
    root.geometry(f"{win_width}x{win_height}+{win_xpos}+{win_ypos}")  # (width x height + XPOS + YPOS on monitor)
    # root.configure(background='black')
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    # Create frames needed for this app ############
    frame_main = tk.LabelFrame(master=root)
    frame_topBanner = tk.LabelFrame(master=frame_main)
    frame_dropdown = tk.LabelFrame(master=frame_topBanner, pady=2)
    frame_search = tk.LabelFrame(master=frame_main, borderwidth=2, pady=5)
    frame_outText = tk.LabelFrame(master=frame_main, borderwidth=2, pady=5, height=50)

    # TOP BANNER ELEMENTS: Title Text and Language Selector (frame_topBanner) ############
    # TOP BANNER 1: Title Text
    label_title = tk.Label(master=frame_topBanner, text="Food Compatibility Search Tool")
    label_title.config(font=("Helvetica", 24))
    label_title.pack(side=tk.TOP)

    # frame_main.grid_rowconfigure(0, weight=1)
    # frame_main.grid_columnconfigure(0, weight=1)

    # TOP BANNER 2: Dropdown Language Selector (frame_dropdown)
    label_lang = tk.Label(master=frame_dropdown, text="Search Language: ")
    label_lang.grid(row=0, column=1)
    optionsList_lang = ['English (EN)', 'Mandarin (ZH)']
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

    # SEARCH BAR ELEMENTS (frame_search) ############
    label_search = tk.Label(master=frame_search, text="Search Text: ")
    label_search.grid(row=0, column=0)
    entry_search = tk.Entry(master=frame_search)
    entry_search.grid(row=0, column=1)
    entry_search.focus_set()

    # On button press, edit the text in the result box.
    def on_button():
        global lang, searchTerm
        searchTerm = entry_search.get()
        searchLang = var_lang.get()
        text_out.config(state=tk.NORMAL)
        # text_out.delete(1.0, tk.END)
        text_out.insert(tk.INSERT, "TEST123\n")
        text_out.config(state=tk.DISABLED)
        if searchLang in optionsList_lang[0]:
            lang = 'en'
        else:
            lang = 'zh'

    button = tk.Button(master=frame_search, text="Search", command=on_button)
    button.grid(row=0, column=2)
    frame_search.pack(side="top")

    # OUTPUT RESULT BOX (frame_outText) ############
    scroll_outText = tk.Scrollbar(master=frame_outText)
    scroll_outText.pack(side=tk.RIGHT, fill=tk.Y)

    text_out = tk.Text(master=frame_outText, wrap=tk.WORD, yscrollcommand=scroll_outText.set)
    text_out.config(font=("helvetica", 14))
    text_out.insert(tk.INSERT, "### Please enter search term in the box above. ###\n")
    text_out.config(state=tk.DISABLED)  # This disables the text editing function inside the text box
    text_out.pack(expand='yes', fill='both')

    scroll_outText.config(command=text_out.yview)
    frame_outText.pack(side='top', fill='both', expand=1, padx=10, pady=10)

    label_credit = tk.Label(master=frame_main)
    label_credit.config(text="Made by Tom Sung [2021]")
    label_credit.pack()

    # Packing the main frame ############
    frame_main.pack(side='top', fill='both', expand='yes', padx=10, pady=10)
    # frame_main.grid(padx=10, pady=10, sticky='nswe')

    # Run the window/app ############
    root.mainloop()


if __name__ == '__main__':
    gui()
    # TODO: Figure out how to prevent elements from getting cut off by restricting text box size
    # TODO: Add search results functionality.
