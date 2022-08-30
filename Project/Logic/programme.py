#library
import tkinter as tk
from tkinter import ttk

#initial
programme = tk.Tk()
programme.geometry("600x400+50+50")
programme.resizable(False, False)
programme.iconbitmap(r'C:\Users\Admin\Documents\Coding\Project\Logic\download (4).ico')
programme.title("Demo ยังทำไม่เสร็จน้าา")
programme['bg'] = '#FFA500'
f = ("Itim", 16)

#enter button
enter_icon = tk.PhotoImage(file=r'C:\Users\Admin\Documents\Coding\Project\Logic\enter_logo.png')
enter_button = ttk.Button(
    programme,
    image=enter_icon,
    text='ENTER',
    compound=tk.LEFT)
enter_button.pack(ipadx=1,ipady=1,expand=True)

#exit button
exit_icon = tk.PhotoImage(file=r'C:\Users\Admin\Documents\Coding\Project\Logic\exit_logo.png')
exit_button = ttk.Button(
    programme,
    image=exit_icon,
    text='EXIT',
    compound=tk.LEFT,
    command=lambda: programme.quit())
exit_button.pack(ipadx=5,ipady=5,expand=True)

#activate
programme.mainloop()