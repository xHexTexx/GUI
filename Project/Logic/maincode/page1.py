#library
import tkinter as tk
from tkinter import ttk

#initial
Page1 = tk.Tk()
Page1.geometry("600x400+50+50")
Page1.resizable(False, False)
Page1.title("Press the options")
Page1.iconbitmap(r'C:\Users\Admin\Documents\Coding\Project\Logic\download (4).ico')

#button1
def go_to_page21() :
    Page1.destroy()
    import page21
button1 = ttk.Button(
    Page1,
    text = "find 1 substance's details",
    command=go_to_page21)
button1.pack(ipadx=1,ipady=1,expand=True)

#button2
def go_to_page22() :
    Page1.destroy()
    import page22
button2 = ttk.Button(
    Page1,
    text = "solve anything in the world",
    command=go_to_page22
)
button2.pack(ipadx=1,ipady=1,expand=True)

#return button
def return_to_hub() :
    Page1.destroy()
    import hub
return_icon = tk.PhotoImage(file=r'C:\Users\Admin\Documents\Coding\Project\Logic\exit_logo.png')
return_button = ttk.Button(
    Page1,
    image=return_icon,
    text = 'return to homepage',
    compound=tk.LEFT,
    command=return_to_hub)
return_button.pack(ipadx=5,ipady=5,expand=True)

#activate
Page1.mainloop()