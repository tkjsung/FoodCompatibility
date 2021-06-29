# gui.py
# Type: Script
# Author: Tom Sung
# Purpose: This python script tests Python GUI

# Import relevant libraries
import tkinter as tk


def gui_test():
    window = tk.Tk()  # Create window
    window.title("Food Compatibility Search Tool")
    window.geometry("400x250")
    window.grid_rowconfigure(4, weight=1)
    window.grid_columnconfigure(1, weight=1)
    frame = tk.Frame(window)  # "window" is the parent window

    lb_title = tk.Label(frame, text="Food Compatibility Search Tool")
    lb_title.config(font=("Helvetica", 24))
    lb_title.grid(row=0, column=0, rowspan=2)
    lb_title.pack()

    label = tk.Label(frame, text="Search Text: ")
    # label.grid(row=2, column=0)
    label.pack(side="left")

    edit = tk.Entry(frame)
    edit.pack(side="left", fill="both", expand=1)
    edit.focus_set()

    button = tk.Button(frame, text="Search")
    button.pack()

    frame.pack(side="top")
    window.mainloop()


if __name__ == '__main__':
    gui_test()
