from ctypes import resize
from pickle import FLOAT
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from turtle import width
from PIL import Image,ImageTk
import csv
from tkinter import messagebox
import csv
import pandas as pd
import numpy as np

main = tk.Tk()
main.geometry("600x400+50+50")
main.resizable(False, False)
main.iconbitmap(r'C:\Users\Admin\Documents\Coding\Project\Logic\443525.ico')
main.title("Analytical Helper")
main['bg'] = "#E9DAC1"

class variables :
    def __init__(self , molarmass , vpermol):
        self.molarmass = 0.0
        self.vpermol = 0.0


var = variables(0 , 0)

        

def compoundConverter(compound_string):
    compound_name = ""
    compound_num = ""
    compound_string += "E"

    str_list = []

    for s in compound_string:
        run = False
        if s=='(' or s==')':
            run = True
        
        if ord('0')<=ord(s) and ord(s)<=ord('9'):
            compound_num += s
        else:
            if (s.upper()==s and (compound_name!="" or compound_num!="")) or run:
                if compound_name=="" and compound_num!="":
                    str_list.append([compound_num, 1])
                    compound_num = ""

                if compound_num!="":
                    # st.append([compound_name, int(compound_num)])
                    str_list.append([compound_name, 0])
                    str_list.append([compound_num, 1])
                elif compound_name!="":
                    # st.append([compound_name, 1])
                    str_list.append([compound_name, 0])
                    str_list.append(['1', 1])

                if not run:
                    compound_name = s
                    compound_num = ""
                else:
                    str_list.append([s, 2])
                    compound_name = ""
                    compound_num = ""
            else:
                compound_name += s

    if compound_num!="":
        str_list.append([compound_num, 1])

    st = []

    for elem in str_list:
        if elem[1]==0:
            st.append([elem[0], 1])
        elif elem[1]==1:
            if st[-1]==')':
                st.pop()
                tmp_st = []
                while st[-1]!='(':
                    st_top = st[-1]
                    st.pop()
                    st_top[1] *= int(elem[0])
                    tmp_st.append(st_top)
                
                st.pop()
                for x in tmp_st:
                    st.append(x)
            else:
                st_top = st[-1]
                st.pop()
                st_top[1] *= int(elem[0])
                st.append(st_top)
        else: 
            st.append(elem[0])

    st.sort()

    for i in range(1, len(st)):
        if st[-i][0]==st[-(i+1)][0]:
            st[-(i+1)][1] += st[-i][1]
            st[-i][1] = 0

    ans = []
    for x in st:
        if x[1]!=0:
            ans.append(x)
    return ans

def searchMolarmass(element, element_list):
    for i in range(0, len(element_list)):
        if element_list[i]==element:
            return i
    return -1

file = open(r'C:\Users\Admin\Documents\Coding\Project\periodic table.csv')
csv_reader = pd.read_csv(file, delimiter=',')
 #-read csv
element = np.array(csv_reader['Element'])
weight = np.array(csv_reader['Weight'])



def cal_molarmass(compound_name):
    ans = compoundConverter(compound_name)
    sum_weight = 0
    for i in ans:
        sum_weight += weight[searchMolarmass(i[0], element)] * i[1]

    return sum_weight


def go_to_page_1() :
    def gas_state2() :
        var.vpermol = float()
        pressure = float(pressure_box.get())
        temp = float(temp_box.get())
        if(checkbox.get() == '1') :
            messagebox.showinfo('Succesfully Set!!!','Succesfully Set!!!')
        if(ps_unit.get() == 'atm') :
            if(temp_unit.get() == '°C') :
                var.vpermol = (0.0821*(temp+273))/pressure
            elif(temp_unit.get() == 'K') :
                var.vpermol = (0.0821*(temp))/pressure
            elif(temp_unit.get() == '°F') :
                var.vpermol = (0.0821*((5*(temp-32)/9))-273)/pressure
        elif(ps_unit.get() == 'Pa') :
            if(temp_unit.get() == '°C') :
                var.vpermol = (0.0821*(temp+273))/(pressure/(1.01325e5))
            elif(temp_unit.get() == 'K') :
                var.vpermol = (0.0821*(temp))/(pressure/(1.01325e5))
            elif(temp_unit.get() == '°F') :
                var.vpermol = (0.0821*((5*(temp-32)/9))-273)/(pressure/(1.01325e5))
        elif(ps_unit.get() == 'psi') :
            if(temp_unit.get() == '°C') :
                var.vpermol = (0.0821*(temp+273))/(pressure/(0.0680459639))
            elif(temp_unit.get() == 'K') :
                var.vpermol = (0.0821*(temp))/(pressure/(0.0680459639))
            elif(temp_unit.get() == '°F') :
                var.vpermol = (0.0821*((5*(temp-32)/9))-273)/(pressure/(0.0680459639))
        elif(ps_unit.get() == 'torr') :
            if(temp_unit.get() == '°C') :
                var.vpermol = (0.0821*(temp+273))/(pressure/(0.00131578947))
            elif(temp_unit.get() == 'K') :
                var.vpermol = (0.0821*(temp))/(pressure/(0.00131578947))
            elif(temp_unit.get() == '°F') :
                var.vpermol = (0.0821*((5*(temp-32)/9))-273)/(pressure/(0.00131578947))
        print(var.vpermol)
    def calculate_mass() :
        mass = mass_input.get()
        mol = float(mass)/float(var.molarmass)
        if (cb_uom.get() == 'gram(g)'):
            if(rsfm.get() == 'volumn at STP') :
                output_text1["text"] = f"{mol*22.4} dm^3"
            elif(rsfm.get() == 'particle') :
                output_text1["text"] = f"{mol*6.02e23} particles"
            elif(rsfm.get() == 'mol') :
                output_text1["text"] = f"{mol} mol"   
        else :
            if(rsfm.get() == 'volumn at STP') :
                output_text1["text"] = f"{mol*22.4/1000} dm^3"
            elif(rsfm.get() == 'particle') :
                output_text1["text"] = f"{mol*6.02e20} particles"
            elif(rsfm.get() == 'mol') :  
                output_text1["text"] = f"{mol/1000} mol"
    def calculate_volumn() :
        volumn = volumn_input.get()
        if (gas_state1.get() == 'STP'):
            mol = float(volumn)/22.4
            if(cb_uom2.get() == 'dm^3') :
                if(rsfv.get() == 'mass') :
                    output_text2["text"] = f"{mol*35.5} gram"
                elif(rsfv.get() == 'particle') :
                    output_text2["text"] = f"{mol*6.02e23} particles"
                elif(rsfv.get() == 'mol') :
                    output_text2["text"] = f"{mol} mol"
            else :
                if(rsfv.get() == 'cm^3') :
                    output_text2["text"] = f"{mol*35.5/1000} gram"
                elif(rsfv.get() == 'particle') :
                    output_text2["text"] = f"{mol*6.02e20} particles"
                elif(rsfv.get() == 'mol') :
                    output_text2["text"] = f"{mol/1000} mol"                  
        else :
            mol = float(volumn)/(var.vpermol)
            if(cb_uom2.get() == 'dm^3') :
                if(rsfv.get() == 'mass') :
                    output_text2["text"] = f"{mol*35.5} gram"
                elif(rsfv.get() == 'particle') :
                    output_text2["text"] = f"{mol*6.02e23} particles"
                elif(rsfv.get() == 'mol') :
                    output_text2["text"] = f"{mol} mol"
            else :
                if(rsfv.get() == 'cm^3') :
                    output_text2["text"] = f"{mol*35.5/1000} gram"
                elif(rsfv.get() == 'particle') :
                    output_text2["text"] = f"{mol*6.02e20} particles"
                elif(rsfv.get() == 'mol') :
                    output_text2["text"] = f"{mol/1000} mol"    
    def compoundConverter(compound_string):
        compound_name = ""
        compound_num = ""
        compound_string += "E"

        str_list = []

        for s in compound_string:
            run = False
            if s=='(' or s==')':
                run = True
            
            if ord('0')<=ord(s) and ord(s)<=ord('9'):
                compound_num += s
            else:
                if (s.upper()==s and (compound_name!="" or compound_num!="")) or run:
                    if compound_name=="" and compound_num!="":
                        str_list.append([compound_num, 1])
                        compound_num = ""

                    if compound_num!="":
                        # st.append([compound_name, int(compound_num)])
                        str_list.append([compound_name, 0])
                        str_list.append([compound_num, 1])
                    elif compound_name!="":
                        # st.append([compound_name, 1])
                        str_list.append([compound_name, 0])
                        str_list.append(['1', 1])

                    if not run:
                        compound_name = s
                        compound_num = ""
                    else:
                        str_list.append([s, 2])
                        compound_name = ""
                        compound_num = ""
                else:
                    compound_name += s

        if compound_num!="":
            str_list.append([compound_num, 1])

        st = []

        for elem in str_list:
            if elem[1]==0:
                st.append([elem[0], 1])
            elif elem[1]==1:
                if st[-1]==')':
                    st.pop()
                    tmp_st = []
                    while st[-1]!='(':
                        st_top = st[-1]
                        st.pop()
                        st_top[1] *= int(elem[0])
                        tmp_st.append(st_top)
                    
                    st.pop()
                    for x in tmp_st:
                        st.append(x)
                else:
                    st_top = st[-1]
                    st.pop()
                    st_top[1] *= int(elem[0])
                    st.append(st_top)
            else: 
                st.append(elem[0])

        st.sort()

        for i in range(1, len(st)):
            if st[-i][0]==st[-(i+1)][0]:
                st[-(i+1)][1] += st[-i][1]
                st[-i][1] = 0

        ans = []
        for x in st:
            if x[1]!=0:
                ans.append(x)
        return ans
    def searchMolarmass(element, element_list):
        for i in range(0, len(element_list)):
            if element_list[i]==element:
                return i
        return -1         
    page1 = tk.Tk()
    page1.geometry("600x400+50+50")
    page1.resizable(False, False)
    page1.title("Analytical Helper")
    page1.iconbitmap(r'C:\Users\Admin\Documents\Coding\Project\Logic\443525.ico')
    
    #text_box
    label = ttk.Label(
    page1,
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
    element_input = ttk.Entry(page1, textvariable = text)
    element_input.pack(ipadx=5,ipady=3,expand=True)
    element_input.place(x=225, y=100)
    element_input.focus()
    def submit() :
        #molar_mass = float(0.0)
        #temp1 = float(0.0)
        #text_permanent = str()
        temp1 = str(element_input.get())
        var.molarmass = cal_molarmass(temp1)
        molarmass_text.config(text = var.molarmass)
        #show_mw.config(text=molar_mass)
    confirm_button = ttk.Button(page1,
    #image=r'C:\Users\Admin\Documents\Coding\Project\Logic\submit_button.jpg',
    text='submit')
    molarmass_text = ttk.Label(page1, text=var.molarmass)
    molarmass_text.place(x=350, y=150)
    confirm_button.pack(ipadx=5,ipady=5,expand=True)
    confirm_button.place(x=400, y=100)
    confirm_button.configure(command=submit)
    
    #mass
    cb_uom = ttk.Combobox(page1, values=['gram(g)', 'kilogram(kg)'], width=5, state="readonly")
    mass_text = tk.Label(page1, text="mass", font=("Kanit", 10))
    output_text1 = tk.Label(page1, font=("Kanit", 10))
    confirm_button3 = ttk.Button(page1,text='submit', command=calculate_mass)
    mass_input = ttk.Entry(page1,width=10)
    cb_uom.place(x=250, y=200)
    mass_text.pack(ipadx=10, ipady=10)
    mass_text.place(x=40, y=195)
    #mass = tk.StringVar()
    mass_input.pack(ipadx=5,ipady=3,expand=True)
    mass_input.place(x=105, y=200)
    output_text1.pack(ipadx=10,ipady=10)
    output_text1.place(x=495, y=195)
    confirm_button3.pack(ipadx=5,ipady=5,expand=True)
    confirm_button3.place(x=320, y=197.5)
    rsfm = ttk.Combobox(page1, values=['mol', 'volumn at STP','volumn at customised', 'particle'], width=5, state="readonly")
    rsfm.place(x=425, y=200)
    #unit_of_mass = tk.StringVar()
    #mol = int()
    #op_text1 = str(mol)

    
    #volumn
    volumn_text = tk.Label(page1, text="volumn", font=("Kanit", 10))
    volumn_text.pack(ipadx=10, ipady=10)
    volumn_text.place(x=40, y=255)
    volumn = tk.StringVar()
    volumn_input = ttk.Entry(page1, textvariable=volumn, width=10)
    volumn_input.pack(ipadx=5,ipady=3,expand=True)
    volumn_input.place(x=165, y=260)
    gas_state1 = ttk.Combobox(page1, values=['STP', 'customised'], width=5, state="readonly")
    gas_state1.place(x=105, y=260)
    cb_uom2 = ttk.Combobox(page1, values=['dm^3', 'cm^3'], width=5, state="readonly")
    cb_uom2.place(x=250, y=260)
    confirm_button4 = ttk.Button(page1,text='submit',command=calculate_volumn)
    confirm_button4.pack(ipadx=5,ipady=5,expand=True)
    confirm_button4.place(x=320, y=260)
    rsfv = ttk.Combobox(page1, values=['mol', 'mass', 'particle'], width=5, state="readonly")
    rsfv.place(x=425, y=260)
    output_text2 = tk.Label(page1, font=("Kanit", 10))
    output_text2.pack(ipadx=10,ipady=10)
    output_text2.place(x=495, y=255)

    #particle
    particle_text = tk.Label(page1, text="particle", font=("Kanit", 10))
    particle_text.pack(ipadx=10, ipady=10)
    particle_text.place(x=40, y=225)
    particle = tk.StringVar()
    particle_input = ttk.Entry(page1, textvariable=particle)
    particle_input.pack(ipadx=5,ipady=3,expand=True)
    particle_input.place(x=105, y=230)
    confirm_button2 = ttk.Button(page1,text='submit')
    confirm_button2.pack(ipadx=5,ipady=5,expand=True)
    confirm_button2.place(x=320, y=230)
    rsfp = ttk.Combobox(page1, values=['mol','mass(g)', 'volumn at STP','volumn at customised'], width=5, state="readonly")
    rsfp.place(x=425, y=227.5)

    #gas state
    var.vpermol = float()
    gas_state = tk.Label(page1, text="gas state", font=("Kanit", 10))
    gas_state.pack(ipadx=10, ipady=10)
    gas_state.place(x=40, y=290)
    pressure_text = tk.Label(page1, text="Pressure (P) :", font=("Kanit", 10))
    pressure_text.place(x=45, y=322.5)
    pressure_box = ttk.Entry(page1, width=10)
    pressure_box.place(x=135, y=325)
    ps_unit = ttk.Combobox(page1, values=['atm','Pa', 'psi','torr'], width=3, state="readonly")
    ps_unit.place(x=205, y=325)
    temp_text = tk.Label(page1, text="Temperature (T) :", font=("Kanit", 10))
    temp_text.place(x=275, y=322.5)
    temp_box = ttk.Entry(page1, width=10)
    temp_box.place(x=385, y=325)
    temp_unit = ttk.Combobox(page1, values=['°C','K', '°F'], width=3, state="readonly")
    temp_unit.place(x=455, y=325)
    checkbox = tk.StringVar()
    state_checkbox = ttk.Button(page1, command=gas_state2)
    state_checkbox.place(x=500, y=325)

    #show_molar_mass
    #text_show_mw = ttk.Label(page1, text='Molar Mass is ',font=("Itim", 12)).place(x=257, y=135)
    #show_mw = ttk.Label(page1, textvariable=show_mw ,font=("Itim", 12))
    #show_mw.place(x=365, y=135)

    #return
    return_icon = tk.PhotoImage(file=r'C:\Users\Admin\Documents\Coding\Project\Logic\exit_logo.png')
    return_button = ttk.Button(
    page1,
    text = 'return to homepage',
    compound=tk.LEFT,
    command=lambda: page1.destroy())
    return_button.pack(ipadx=1,ipady=1,expand=True)
    return_button.place(x=15, y=15)

def go_to_page_2() :
    def create() :
        def fill_unit1(event) :
            if(rxt_type.get() == 'mass') :
                rxt_unit['values'] = ['gram(g)', 'kilogram(kg)']
            elif(rxt_type.get() == 'particle') :
                rxt_unit['values'] = ['atom', 'molecule']
            elif(rxt_type.get() == 'volumn at STP' or rxt_type.get() == 'volumn(custom)') :
                rxt_unit['values'] = ['dm^3', 'cm^3']
        def fill_unit2(event) :
            if(pro_type.get() == 'mass') :
                pro_unit['values'] = ['gram(g)', 'kilogram(kg)']
            elif(pro_type.get() == 'particle') :
                pro_unit['values'] = ['atom', 'molecule']
            elif(pro_type.get() == 'volumn at STP' or pro_type.get() == 'volumn(custom)') :
                pro_unit['values'] = ['dm^3', 'cm^3']
        reactant_text = tk.Label(page2, text="reactants :")
        product_text = tk.Label(page2, text="products :")
        reactant_text.place(x=45, y=97.5)
        product_text.place(x=45, y=297.5)
        for i in range(int(n_of_reactant.get())) :
            rxt_dt = ttk.Entry(page2, width=4)
            reactant = ttk.Entry(page2, width=11)
            bl1 = ttk.Entry(page2, width=2)
            rxt_type = ttk.Combobox(page2, 
                            values=['mass', 'particle', 'volumn at STP', 'volumn(custom)'],
                            width=1, state="readonly")
            rxt_unit = ttk.Combobox(page2, values='', width=1, state="readonly")
            reactant.place(x=135+(100*i), y=100)
            bl1.place(x=115+(100*i), y=100)
            rxt_type.place(x=115+(100*i), y=125)
            rxt_dt.place(x=145.5+(100*i), y=125)
            rxt_unit.place(x=177.5+(100*i), y=125)
            rxt_type.bind('<<ComboboxSelected>>', fill_unit1)
        for i in range(int(n_of_product.get())) :
            product = ttk.Entry(page2, width=11)
            bl2 = ttk.Entry(page2, width=2)
            pro_type = ttk.Combobox(page2, values=['mass', 'particle', 'volumn at STP', 'volumn(custom)'], width=1, state="readonly")
            pro_dt = ttk.Entry(page2, width=4)
            pro_unit = ttk.Combobox(page2, values=[], width=1, state="readonly")
            product.place(x=135+(100*i), y=300)
            bl2.place(x=115+(100*i), y=300)
            pro_type.place(x=115+(100*i), y=325)
            pro_dt.place(x=145.5+(100*i), y=325)
            pro_unit.place(x=177.5+(100*i), y=325)   
            pro_type.bind('<<ComboboxSelected>>', fill_unit2)     
    page2 = tk.Tk()
    page2.geometry("750x450+50+50")
    page2.resizable(False, False)
    page2.title("Analytical Helper")
    page2.iconbitmap(r'C:\Users\Admin\Documents\Coding\Project\Logic\443525.ico')
    type_1 = []
    n1 = tk.StringVar()
    #reactant
    enter_n_of_reactant = tk.Label(page2, text="number of reactant :", font=("Kanit", 10), textvariable=n1)
    enter_n_of_reactant.place(x=100, y=50)
    n_of_reactant = ttk.Spinbox(page2, from_=1, to=6, wrap=True, width=3)
    n_of_reactant.place(x=245, y=55)

    #product
    enter_n_of_product = tk.Label(page2, text="number of product :", font=("Kanit", 10))
    enter_n_of_product.place(x=325, y=50)
    n_of_product = ttk.Spinbox(page2, from_=1, to=6, wrap=True, width=3)
    n_of_product.place(x=465, y=55)

    #command
    balance_button = ttk.Button(page2,text='balance')
    balance_button.place(x=315, y=200)
    calculate_button = ttk.Button(page2,text='calculate')
    calculate_button.place(x=420, y=200)
    #command
    confirm_button = ttk.Button(page2,text='submit',command=create)
    confirm_button.pack(ipadx=5,ipady=5,expand=True)
    confirm_button.place(x=525, y=52.5)    
    clear_button = ttk.Button(page2,text='clear')
    clear_button.place(x=605, y=52.5)

    #return
    return_icon = tk.PhotoImage(file=r'C:\Users\Admin\Documents\Coding\Project\Logic\exit_logo.png')
    return_button = ttk.Button(
    page2,
    text = 'return to homepage',
    compound=tk.LEFT,
    command=lambda: page2.destroy())
    return_button.pack(ipadx=1,ipady=1,expand=True)
    return_button.place(x=15, y=15)

enter_icon = Image.open(r"C:\Users\Admin\Documents\Coding\Project\Logic\enter_logo.png")
resized_enter_icon = enter_icon.resize((50, 50))
use_resized_enter_icon = ImageTk.PhotoImage(resized_enter_icon)
enter_button = ttk.Button(
    main,
    image=use_resized_enter_icon,
    text='      ENTER PAGE I',
    compound=tk.LEFT,
    command=go_to_page_1)
enter_button.pack(ipadx=4,ipady=4,expand=True)

enter_icon2 = Image.open(r"C:\Users\Admin\Documents\Coding\Project\Logic\enter_logo.png")
resized_enter_icon2 = enter_icon.resize((50, 50))
use_resized_enter_icon2 = ImageTk.PhotoImage(resized_enter_icon2)
enter_button = ttk.Button(
    main,
    image=use_resized_enter_icon2,
    text='      ENTER PAGE II',
    compound=tk.LEFT,
    command=go_to_page_2)
enter_button.pack(ipadx=4,ipady=8,expand=True)

exit_icon = Image.open(r"C:\Users\Admin\Documents\Coding\Project\Logic\exit_logo.png")
resized_exit_icon = exit_icon.resize((50, 50))
use_resized_exit_icon = ImageTk.PhotoImage(resized_exit_icon)
exit_button = ttk.Button(
    main,
    image=use_resized_exit_icon,
    text='      FAREWELL',
    compound=tk.LEFT,
    command=lambda: main.quit())
exit_button.pack(ipadx=4,ipady=12,expand=True)

main.mainloop()