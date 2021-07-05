# gui.py
# Type: Script
# Author: Tom Sung
# Purpose: This python script tests Python GUI

# Import relevant libraries
import tkinter as tk


def gui_test():
    root = tk.Tk()  # Create window
    root.title("Food Compatibility Search Tool")
    root.geometry("400x250+400+200")  # (width x height + XPOS on monitor + YPOS on monitor
    # window.grid_rowconfigure(4, weight=1)
    # window.grid_columnconfigure(1, weight=1)
    # frame = tk.Frame(master=root, borderwidth=2)  # "window" is the parent window
    # frame.grid(row=1, column=1, padx=5, pady=1)
    lb_title = tk.Label(master=root, text="Food Compatibility Search Tool")
    lb_title.config(font=("Helvetica", 24))
    # lb_title.grid(row=0, column=0, rowspan=2)
    lb_title.pack(pady=30)

    frame = tk.Frame(master=root, borderwidth=2)  # "window" is the parent window
    # frame.grid(row=2, column=1, padx=5, pady=1)
    label = tk.Label(master=frame, text="Search Text: ")
    label.grid(row=0, column=0)
    # label.pack(side="left")

    edit = tk.Entry(master=frame)
    edit.grid(row=0, column=1)
    # edit.pack(side="left")
    # edit.pack(side="left", fill="both", expand=1)
    edit.focus_set()
    frame.pack()

    button = tk.Button(master=root, text="Search")
    button.pack()

    # frame.pack(side="top")
    root.mainloop()


def gui_training():
    root = tk.Tk()
    root.title("GUI Testing Code")
    root.geometry("400x400+400+250")
    # for i in range(5):
    #     root.grid_columnconfigure(i, weight=1)
    # for j in range(3):
    #     root.grid_rowconfigure(j, weight=1)
    # screen_width = root.winfo_screenwidth()
    # screen_height = root.winfo_screenheight()

    frame = tk.Frame(master=root, borderwidth=1)
    frame.grid(row=1, column=1)
    label = tk.Label(master=frame, text="test1")
    label.pack()
    frame = tk.Frame(master=root, borderwidth=1)
    frame.grid(row=2, column=1)
    label = tk.Label(master=frame, text="test2")
    label.pack()
    frame = tk.Frame(master=root, borderwidth=1)
    frame.grid(row=4, column=2)
    label = tk.Label(master=frame, text="test3")
    label.pack()
    frame = tk.Frame(master=root, borderwidth=1)
    frame.grid(row=0, column=3)
    label = tk.Label(master=frame, text="test4")
    label.pack()

    """
    for i in range(2):
        for j in range(3):
            frame = tk.Frame(
                master=root,
                relief=tk.RAISED,
                borderwidth=1
            )
            frame.grid(row=i, column=j)
            label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
            label.pack()
    """

    # label = tk.Label(root, text="This is a test")
    # label.pack()
    root.mainloop()


if __name__ == '__main__':
    gui_test()
    # gui_training()
