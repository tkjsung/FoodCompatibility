# gui.py
# Type: Script
# Author: Tom Sung
# Purpose: This python script tests Python GUI

# Import relevant libraries
import tkinter as tk


lang = ''


def gui_test():
    # Window Size ############
    win_width = 900
    win_height = 500
    win_xpos = 370
    win_ypos = 200

    # Create window ############
    root = tk.Tk()
    root.title("Food Compatibility Search Tool")
    root.geometry(f"{win_width}x{win_height}+{win_xpos}+{win_ypos}")  # (width x height + XPOS + YPOS on monitor)
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    # Title Text ############
    lb_title = tk.Label(master=root, text="Food Compatibility Search Tool")
    lb_title.config(font=("Helvetica", 24))
    # lb_title.grid(row=0, column=0, rowspan=2)
    lb_title.pack(pady=30)

    # Frame for containing search bar ############
    frame = tk.LabelFrame(master=root, borderwidth=2, pady=5)
    label = tk.Label(master=frame, text="Search Text: ")
    label.grid(row=0, column=0)
    # label.pack(side="left")

    # Search box (within Frame) ############
    edit = tk.Entry(master=frame)
    edit.grid(row=0, column=1)
    # edit.pack(side="left", fill="both", expand=1)
    edit.focus_set()  # Without focus_set, the user would have to click into the search box

    # On button press, edit the text in the result box.
    def on_button():
        # global searchTerm
        searchTerm = edit.get()
        output.config(state=tk.NORMAL)
        output.insert(tk.INSERT, searchTerm)
        output.insert(tk.INSERT, "\n")
        output.config(state=tk.DISABLED)
        # searchTerm = "This is a test"

    # Button for search (within Frame) ############
    button = tk.Button(master=frame, text="Search", command=on_button)
    button.grid(row=0, column=2)  # If grid exists for geometry, cannot use pack
    # button.pack()
    frame.pack(side="top")  # This frame is complete. Packed.

    # New frame to contain result output text box [frame1] ############
    # TODO: Text box should be wider. Research into making it wider via frame1 adjustment
    frame1 = tk.LabelFrame(master=root, borderwidth=2, pady=5)

    # In frame1, create a scroll wheel for the results. ############
    scroll = tk.Scrollbar(command=frame1)
    scroll.pack(side=tk.RIGHT, fill=tk.Y)

    # In frame1, create a text box to contain the results ############
    output = tk.Text(master=frame1, wrap=tk.WORD, yscrollcommand=scroll.set)
    output.config(font=("Helvetica", 14))
    # for i in range(0, 100):
    #     output.insert(tk.INSERT, "test123\n")
    # output.insert(tk.END, "test12312")  # This is how you insert text into the GUI.
    output.insert(tk.INSERT, "### Please enter search term in the box above. ###\n")
    output.config(state=tk.DISABLED)  # This disables the text editing function inside the text box
    output.pack()

    # After the text inside the result output box is written and packed, specify where scroll wheel should be used ############
    scroll.config(command=output.yview)
    # frame1.pack()
    frame1.pack(side="top", fill="both", expand="yes", padx=10, pady=10)

    # Temporary placed after text box to see if it shows up. Probably will keep this creation text ############
    lb_copyright = tk.Label(master=root)
    lb_copyright.config(text="Copyright © 2021 Ke-Jun Sung")
    lb_copyright.pack()

    # root_scroll.config(command=root.yview)  # Frames (and windows, for that matter) do not have yview attribute
    # Consider using tk.Canvas.
    root.mainloop()
    print("test123")


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


def gui_canvas():
    root = tk.Tk()
    root.title("Tkinter Canvas Test")
    root.geometry("700x500+370+200")  # (width x height + XPOS on monitor + YPOS on monitor
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    w = tk.Canvas(master=root)
    scroll = tk.Scrollbar(command=w)
    scroll.pack(side=tk.RIGHT, fill=tk.Y)

    for i in range(0, 100):
        tk.Label(master=w, text="This is a test\n").pack()

    scroll.config(command=w.yview)
    w.pack()
    root.mainloop()


def gui_frameInframe():
    root = tk.Tk()
    root.title("Test Frame in Frame")
    root.geometry("700x500+370+200")  # (width x height + XPOS on monitor + YPOS on monitor
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    main_frame = tk.LabelFrame(master=root)

    canvas = tk.Canvas(master=main_frame)
    canvas.pack(side=tk.LEFT, fill="both", expand="yes")

    scroll = tk.Scrollbar(master=main_frame, command=canvas.yview)
    scroll.pack(side=tk.RIGHT, fill=tk.Y)

    canvas.config(yscrollcommand=scroll.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.bind_all("<MouseWheel>", lambda e: canvas.yview_scroll(-1*int((e.delta/120)), "units"))

    sub_frame1 = tk.LabelFrame(master=canvas)
    # sub_frame1.pack(side="top", fill="both", expand='yes', padx=100, pady=10)  # This will do nothing b/c...
    # ...sub_frame1 is being added to a window in the Canvas.
    # root.update()
    # canvas.update()
    canvas_width = canvas.winfo_reqwidth()
    canvas_height = canvas.winfo_reqheight()
    canvas.create_window((0, 0), window=sub_frame1, anchor="n")

    for i in range(0, 100):
        tk.Label(master=sub_frame1, text=f"This is a test {i+1}").pack()

    main_frame.pack(side="top", fill="both", expand="yes", padx=10, pady=10)
    root.mainloop()


def gui_searchButton():
    def on_button():
        searchTerm = entry.get()
        print(searchTerm)
    root = tk.Tk()
    entry = tk.Entry(master=root)
    button = tk.Button(master=root, text="Get", command=on_button)
    # button = tk.Button(master=root, text="Get", command=(lambda e=entry: entry.get()))
    entry.pack(side=tk.LEFT)
    button.pack(side=tk.LEFT)
    root.mainloop()
    print("test123")


def gui_choice():
    # Window Size ############
    win_width = 900
    win_height = 500
    win_xpos = 370
    win_ypos = 200

    # Create window ############
    root = tk.Tk()
    root.title("Food Compatibility Search Tool")
    root.geometry(f"{win_width}x{win_height}+{win_xpos}+{win_ypos}")  # (width x height + XPOS + YPOS on monitor)
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    main_frame = tk.LabelFrame(master=root)
    frame = tk.LabelFrame(master=main_frame)

    label = tk.Label(master=frame, text="Language: ")
    # label.pack(side=tk.TOP, anchor="ne")
    # label.pack()
    label.grid(row=0, column=0)

    OPTIONS = ["English (EN)", "Mandarin (ZH)"]

    variable = tk.StringVar(master=frame)
    variable.set(OPTIONS[0])
    option = tk.OptionMenu(frame, variable, *OPTIONS)
    # option.pack()
    option.grid(row=0, column=1)
    # option.pack(side=tk.TOP, anchor="ne")

    label1 = tk.Label(master=main_frame, text="asdasdfadsffadsfad")

    def on_button():
        global lang
        result = variable.get()
        # print(len(OPTIONS))
        # logic = result in OPTIONS[0]
        # print(logic)
        if result in OPTIONS[0]:
            lang = 'en'
        else:
            lang = 'zh'

    button = tk.Button(master=main_frame, text="OK", command=on_button)

    frame.pack(side=tk.TOP, anchor="ne")
    # frame.grid(row=0, column=1)

    # label1.grid(row=1)
    label1.pack()
    button.pack(side="top")

    main_frame.pack(side="top", fill="both", expand="yes", padx=10, pady=10)
    root.mainloop()
    # print("test123")


if __name__ == '__main__':
    # gui_test()
    # gui_scrollbar()
    # gui_training()
    # gui_canvas()
    # gui_frameInframe()
    # gui_searchButton()
    gui_choice()
    print("123")
    # TODO: Forget about using Canvas to scroll the entire app.
    #   Either find a third-party library that does scrolling easier (don't use Tkinter)
    #   Or manipulate existing stuff to scroll
