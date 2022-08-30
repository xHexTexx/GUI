#library
from ast import Str
from dataclasses import replace
import tkinter as tk
from tkinter import ttk
from unittest import result
from xml.dom.minidom import Element
import pandas as pd
import numpy as np
import csv

#initial
Page21 = tk.Tk()
Page21.geometry("600x400+50+50")
Page21.resizable(False, False)
Page21.title("Let's Find It!!!")
Page21.iconbitmap(r'C:\Users\Admin\Documents\Coding\Project\Logic\download (4).ico')
label = ttk.Label(
    Page21,
    text="Enter what you'd like to",
    font=("Itim", 16))
label.pack(ipadx=10, ipady=10)
label.place(x=200, y=50)
    #-file csv
file = open(r'C:\Users\Admin\Documents\Coding\Project\periodic table.csv')
csv_reader = csv.reader(file, delimiter=',')
    #-read csv
element = []
weight = []
for row in csv_reader:
    element.append(row[1])
    weight.append(row[2])
lenght_element = len(element)
lenght_weight = len(weight)

#compound's name
text = tk.StringVar()
element_input = ttk.Entry(Page21, textvariable = text)
element_input.pack(ipadx=5,ipady=3,expand=True)
element_input.place(x=225, y=100)
element_input.focus()
molar_mass = float(0.0)
temp1 = float(0.0)
text_permanent = str()
def find_mw(a) :
    for i in range(lenght_element):
        if(element[i] == text.get()) :
            return weight[i]
def submit() :
    temp1 = str(text.get())
    molar_mass = find_mw(temp1)
    show_mw.config(text=molar_mass)
    """text_permanent = text.get()
    for i in range(lenght_element):
        if(element[i] == text.get()) :
            molar_mass = weight[i]
            show_mw.config(text=molar_mass)
            break"""          
confirm_button = ttk.Button(Page21,
    #image=r'C:\Users\Admin\Documents\Coding\Project\Logic\submit_button.jpg',
    text='submit')
confirm_button.pack(ipadx=5,ipady=5,expand=True)
confirm_button.place(x=400, y=100)
confirm_button.configure(command=submit)
    #-try
    
#get details
details = tk.StringVar()
result = float(0.0)
details_input = ttk.Entry(Page21, textvariable=details)
details_input.pack(ipadx=5,ipady=3,expand=True)
details_input.place(x=105, y=170)
def find_from_mass() :
    """for i in range(lenght_element):
        if(element[i] == text_permanent) :
            molar_mass = weight[i]
            break"""
    value = float(details.get())
    #result = value/float(molar_mass)
    show_result_mol.config(text=str(molar_mass))
confirm_button2 = ttk.Button(Page21,text='submit')
confirm_button2.pack(ipadx=5,ipady=5,expand=True)
confirm_button2.place(x=250, y=170)
confirm_button2.configure(command=find_from_mass)
##particle
particle = tk.StringVar
particle_input = ttk.Entry(Page21, textvariable=particle)
particle_input.pack(ipadx=5,ipady=3,expand=True)
particle_input.place(x=105, y=200)
confirm_button3 = ttk.Button(Page21,text='submit')
confirm_button3.pack(ipadx=5,ipady=5,expand=True)
confirm_button3.place(x=250, y=200)
##volumn
volumn = tk.StringVar
volumn_input = ttk.Entry(Page21, textvariable=volumn)
volumn_input.pack(ipadx=5,ipady=3,expand=True)
volumn_input.place(x=105, y=230)
confirm_button4 = ttk.Button(Page21,text='submit')
confirm_button4.pack(ipadx=5,ipady=5,expand=True)
confirm_button4.place(x=250, y=230)

#show details
##show_molar_mass
text_show_mw = ttk.Label(Page21, text='Molar Mass is ',font=("Itim", 12)).place(x=257, y=135)
show_mw = ttk.Label(Page21,font=("Itim", 12))
show_mw.place(x=365, y=135)
##show 1result
show_result_mol = ttk.Label(Page21)#text=str(int(details.get(), base=0)/molar_mass))
show_result_mol.pack(ipadx=5,ipady=3)
show_result_mol.place(x=400, y=170)
##particle
##-logic
#result_mol = int(mass)/molar_mass
##-widget

    
#activate
Page21.mainloop()