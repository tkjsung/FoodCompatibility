# gui.py
# Type: Script
# Author: Tom Sung
# Purpose: This python script tests Python GUI

# Import relevant libraries
import tkinter as tk


def gui_test():
    # Create window
    root = tk.Tk()
    root.title("Food Compatibility Search Tool")
    root.geometry("700x500+370+200")  # (width x height + XPOS on monitor + YPOS on monitor
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    # Testing code... see if entire window scrolling is possible.
    root_scroll = tk.Scrollbar(command=root)
    root_scroll.pack(side=tk.RIGHT, fill=tk.Y)
    # scroll = tk.Scrollbar(command=frame1)
    # scroll.pack(side=tk.RIGHT, fill=tk.Y)


    # Title Text
    lb_title = tk.Label(master=root, text="Food Compatibility Search Tool")
    lb_title.config(font=("Helvetica", 24))
    # lb_title.grid(row=0, column=0, rowspan=2)
    lb_title.pack(pady=30)

    # Frame for containing search bar
    frame = tk.Frame(master=root, borderwidth=2, pady=5)
    label = tk.Label(master=frame, text="Search Text: ")
    label.grid(row=0, column=0)
    # label.pack(side="left")

    # Search box (within Frame)
    edit = tk.Entry(master=frame)
    edit.grid(row=0, column=1)
    # edit.pack(side="left", fill="both", expand=1)
    edit.focus_set()  # Without focus_set, the user would have to click into the search box

    # Button for search (within Frame)
    button = tk.Button(master=frame, text="Search")
    button.grid(row=0, column=2)  # If grid exists for geometry, cannot use pack
    # button.pack()

    frame.pack(side="top")  # This frame is complete. Packed.

    # New frame to contain result output text box [frame1]
    frame1 = tk.Frame(master=root, borderwidth=2, pady=5)

    # In frame1, create a scroll wheel for the results.
    scroll = tk.Scrollbar(command=frame1)
    scroll.pack(side=tk.RIGHT, fill=tk.Y)

    # In frame1, create a text box to contain the results
    output = tk.Text(master=frame1, wrap=tk.NONE, yscrollcommand=scroll.set)
    output.config(font=("Helvetica", 14))
    for i in range(0, 100):
        output.insert(tk.INSERT, "test123\n")
    output.insert(tk.END, "test12312")  # This is how you insert text into the GUI.
    output.config(state=tk.DISABLED)  # This disables the text editing function inside the text box
    output.pack()

    # After the text inside the result output box is written and packed, specify where scroll wheel should be used
    scroll.config(command=output.yview)
    frame1.pack()

    # Temporary placed after text box to see if it shows up. Probably will keep this creation text
    lb_copyright = tk.Label(master=root)
    lb_copyright.config(text="Copyright © 2021 Ke-Jun Sung")
    lb_copyright.pack()

    # root_scroll.config(command=root.yview)  # Frames (and windows, for that matter) do not have yview attribute
    # Consider using tk.Canvas.
    root.mainloop()
    # TODO: Try Canvas by copying the gui_test() function into a new function and see if Canvas can
    #       do scrolling


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


def gui_scrollbar():
    root = tk.Tk()

    # Vertical (y) Scroll Bar
    scroll = tk.Scrollbar(master=root)
    scroll.pack(side=tk.RIGHT, fill=tk.Y)

    # Text Widget
    eula = tk.Text(master=root, wrap=tk.NONE, yscrollcommand=scroll.set)
    for i in range(0, 100):
        eula.insert(tk.INSERT, "text\n")
    # eula.insert(tk.INSERT, "text")
    eula.pack(side="left")

    # Configure the scrollbars
    scroll.config(command=eula.yview)
    root.mainloop()


if __name__ == '__main__':
    gui_test()
    # gui_scrollbar()
    # gui_training()
