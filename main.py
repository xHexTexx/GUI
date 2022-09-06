import tkinter as tk
from tkinter import ttk
from tkinter import *
from Compound_converter import Compound_converter as ccv
from PIL import Image,ImageTk
from balanced_equation import balance
import pandas as pd
import numpy as np

file = open(r'periodic table.csv')
csv_reader = pd.read_csv(file, delimiter=',')
element = np.array(csv_reader['Element'])
weight = np.array(csv_reader['Weight'])

class App(tk.Tk):

    def __init__(self):
        super().__init__()

        self.geometry("600x400+50+50")
        self.resizable(False, False)
        self.iconbitmap(r'Project/Logic/443525.ico')
        self.title("Analytical Helper")
        self['bg'] = "#E9DAC1"
        self.molarmass = 0.0
        self.vpermol = 0.0
        self.reactant_entry = []
        self.product_entry = []
        self.reactant_data = []
        self.product_data = []


class page_button(ttk.Button) :

    def __init__(self , *args , **kwargs):
        Button.__init__(self , *args , **kwargs)

class page_label(ttk.Label) :

    def __init__(self , *args , **kwargs):
        Label.__init__(self , *args , **kwargs)

class page_entry(ttk.Entry) :

    def __init__(self, *args, **kwargs):
        Entry.__init__(self, *args, **kwargs)

class group_entry_reactant:

    def __init__(self , parent , id, *args, **kwargs):
        self.id = id

        def fill_unit1(event):

            if (self.rxt_type.get() == 'mass'):
                self.rxt_unit['values'] = ['gram(g)', 'kilogram(kg)']
            elif (self.rxt_type.get() == 'particle'):
                self.rxt_unit['values'] = ['atom', 'molecule']
            elif (self.rxt_type.get() == 'volumn at STP' or self.rxt_type.get() == 'volumn(custom)'):
                self.rxt_unit['values'] = ['dm^3', 'cm^3']

        self.bl1 = ttk.Entry(parent, width=2 )
        self.bl1.place(x=115 + (100 * id), y=100)


        self.reactant = ttk.Entry(parent, width=11)
        self.rxt_dt = ttk.Entry(parent, width=4)

        self.rxt_type = ttk.Combobox(parent, values=['mass', 'particle', 'volumn at STP', 'volumn(custom)'],width=1, state="readonly"  )
        self.rxt_unit = ttk.Combobox(parent, values='', width=1, state="readonly")

        self.reactant.place(x=135 + (100 * id), y=100)
        self.rxt_type.place(x=115 + (100 * id), y=125)
        self.rxt_dt.place(x=145.5 + (100 * id), y=125)
        self.rxt_unit.place(x=177.5 + (100 * id), y=125)
        self.rxt_type.bind('<<ComboboxSelected>>', fill_unit1)
        self.reactant_text = tk.Label(parent, text="reactants :")
        self.product_text = tk.Label(parent, text="products :")
        self.reactant_text.place(x=45, y=97.5)
        self.product_text.place(x=45, y=297.5)

class group_entry_product:

    def __init__(self , parent , id, *args, **kwargs):
        self.id = id

        def fill_unit2(event) :
            if(self.pro_type.get() == 'mass') :
                self.pro_unit['values'] = ['gram(g)', 'kilogram(kg)']
            elif(self.pro_type.get() == 'particle') :
                self.pro_unit['values'] = ['atom', 'molecule']
            elif(self.pro_type.get() == 'volumn at STP' or self.pro_type.get() == 'volumn(custom)') :
                self.pro_unit['values'] = ['dm^3', 'cm^3']

        self.bl2 = ttk.Entry(parent, width=2)
        self.bl2.place(x=115 + (100 * id), y=300)

        self.product = ttk.Entry(parent, width=11)
        self.pro_dt = ttk.Entry(parent, width=4)
        self.pro_type = ttk.Combobox(parent, values=['mass', 'particle', 'volumn at STP', 'volumn(custom)'], width=1,state="readonly")
        self.pro_unit = ttk.Combobox(parent, values=[], width=1, state="readonly")

        self.product.place(x=135 + (100 * id), y=300)
        self.pro_type.place(x=115 + (100 * id), y=325)
        self.pro_dt.place(x=145.5 + (100 * id), y=325)
        self.pro_unit.place(x=177.5 + (100 * id), y=325)
        self.pro_type.bind('<<ComboboxSelected>>', fill_unit2)

def page1 ():

    page1 = App()

    def searchMolarmass(element, element_list):
        for i in range(0, len(element_list)):
            if element_list[i] == element:
                return i
        return -1

    def cal_molarmass(compound_name):
        ans = ccv(compound_name)
        sum_weight = 0
        for i in ans:
            sum_weight += weight[searchMolarmass(i[0], element)] * i[1]

        return sum_weight

    def calculate_mass():
        mass = mass_input.get()
        mol = float(mass) / float(page1.molarmass)
        if (cb_uom.get() == 'gram(g)'):
            if (rsfm.get() == 'volumn at STP'):
                output_text1["text"] = f"{mol * 22.4} dm^3"
            elif (rsfm.get() == 'particle'):
                output_text1["text"] = f"{mol * 6.02e23} particles"
            elif (rsfm.get() == 'mol'):
                output_text1["text"] = f"{mol} mol"
        else:
            if (rsfm.get() == 'volumn at STP'):
                output_text1["text"] = f"{mol * 22.4 / 1000} dm^3"
            elif (rsfm.get() == 'particle'):
                output_text1["text"] = f"{mol * 6.02e20} particles"
            elif (rsfm.get() == 'mol'):
                output_text1["text"] = f"{mol / 1000} mol"

    def gas_state2():
        page1.vpermol = float()
        pressure = float(pressure_box.get())
        temp = float(temp_box.get())
        if (ps_unit.get() == 'atm'):
            if (temp_unit.get() == '°C'):
                page1.vpermol = (0.0821 * (temp + 273)) / pressure
            elif (temp_unit.get() == 'K'):
                page1.vpermol = (0.0821 * (temp)) / pressure
            elif (temp_unit.get() == '°F'):
                page1.vpermol = (0.0821 * ((5 * (temp - 32) / 9)) - 273) / pressure
        elif (ps_unit.get() == 'Pa'):
            if (temp_unit.get() == '°C'):
                page1.vpermol = (0.0821 * (temp + 273)) / (pressure / (1.01325e5))
            elif (temp_unit.get() == 'K'):
                page1.vpermol = (0.0821 * (temp)) / (pressure / (1.01325e5))
            elif (temp_unit.get() == '°F'):
                page1.vpermol = (0.0821 * ((5 * (temp - 32) / 9)) - 273) / (pressure / (1.01325e5))
        elif (ps_unit.get() == 'psi'):
            if (temp_unit.get() == '°C'):
                page1.vpermol = (0.0821 * (temp + 273)) / (pressure / (0.0680459639))
            elif (temp_unit.get() == 'K'):
                page1.vpermol = (0.0821 * (temp)) / (pressure / (0.0680459639))
            elif (temp_unit.get() == '°F'):
                page1.vpermol = (0.0821 * ((5 * (temp - 32) / 9)) - 273) / (pressure / (0.0680459639))
        elif (ps_unit.get() == 'torr'):
            if (temp_unit.get() == '°C'):
                page1.vpermol = (0.0821 * (temp + 273)) / (pressure / (0.00131578947))
            elif (temp_unit.get() == 'K'):
                page1.vpermol = (0.0821 * (temp)) / (pressure / (0.00131578947))
            elif (temp_unit.get() == '°F'):
                page1.vpermol = (0.0821 * ((5 * (temp - 32) / 9)) - 273) / (pressure / (0.00131578947))
        print(page1.vpermol)

    def calculate_volumn():
        volumn = volumn_input.get()
        if (gas_state1.get() == 'STP'):
            mol = float(volumn) / 22.4
            if (cb_uom2.get() == 'dm^3'):
                if (rsfv.get() == 'mass'):
                    output_text2["text"] = f"{mol * page1.molarmass} gram"
                elif (rsfv.get() == 'particle'):
                    output_text2["text"] = f"{mol * 6.02e23} particles"
                elif (rsfv.get() == 'mol'):
                    output_text2["text"] = f"{mol} mol"
            else:
                if (rsfv.get() == 'cm^3'):
                    output_text2["text"] = f"{mol * page1.molarmass / 1000} gram"
                elif (rsfv.get() == 'particle'):
                    output_text2["text"] = f"{mol * 6.02e20} particles"
                elif (rsfv.get() == 'mol'):
                    output_text2["text"] = f"{mol / 1000} mol"
        else:
            mol = float(volumn) / (page1.vpermol)
            if (cb_uom2.get() == 'dm^3'):
                if (rsfv.get() == 'mass'):
                    output_text2["text"] = f"{mol * page1.molarmass} gram"
                elif (rsfv.get() == 'particle'):
                    output_text2["text"] = f"{mol * 6.02e23} particles"
                elif (rsfv.get() == 'mol'):
                    output_text2["text"] = f"{mol} mol"
            else:
                if (rsfv.get() == 'cm^3'):
                    output_text2["text"] = f"{mol * page1.molarmass / 1000} gram"
                elif (rsfv.get() == 'particle'):
                    output_text2["text"] = f"{mol * 6.02e20} particles"
                elif (rsfv.get() == 'mol'):
                    output_text2["text"] = f"{mol / 1000} mol"

    def submit():

        temp1 = str(element_input.get())
        page1.molarmass = cal_molarmass(temp1)
        molarmass_text.config(text=page1.molarmass)
        molarmass_text.config(text=page1.molarmass)

    # text_box
    label = page_label(page1, text="Enter what you'd like to", font=("Itim", 16))
    label.pack(ipadx=10, ipady=10)
    label.place(x=200, y=50)

    # compound's name
    text = tk.StringVar()
    element_input = page_entry(page1, textvariable=text)
    element_input.pack(ipadx=5, ipady=3, expand=True)
    element_input.place(x=225, y=100)

    confirm_button = page_button(page1,text='submit')
    confirm_button.pack(ipadx=5, ipady=5, expand=True)
    confirm_button.place(x=400, y=100)
    confirm_button.configure(command = submit)

    molarmass_text = page_label(page1, text = "0")
    molarmass_text.place(x=350, y=150)


    # mass
    cb_uom = ttk.Combobox(page1, values=['gram(g)', 'kilogram(kg)'], width=5, state="readonly")
    mass_text = tk.Label(page1, text="mass", font=("Kanit", 10))
    output_text1 = tk.Label(page1, font=("Kanit", 10))
    confirm_button3 = ttk.Button(page1, text='submit', command=calculate_mass)
    mass_input = ttk.Entry(page1, width=10)
    cb_uom.place(x=250, y=200)
    mass_text.pack(ipadx=10, ipady=10)
    mass_text.place(x=40, y=195)

    # mass = tk.StringVar()
    mass_input.pack(ipadx=5, ipady=3, expand=True)
    mass_input.place(x=105, y=200)
    output_text1.pack(ipadx=10, ipady=10)
    output_text1.place(x=495, y=195)
    confirm_button3.pack(ipadx=5, ipady=5, expand=True)
    confirm_button3.place(x=320, y=197.5)
    rsfm = ttk.Combobox(page1, values=['mol', 'volumn at STP', 'volumn at customised', 'particle'], width=5,state="readonly")
    rsfm.place(x=425, y=200)

    unit_of_mass = tk.StringVar()
    mol = int()
    op_text1 = str(mol)

    # volumn
    volumn_text = tk.Label(page1, text="volumn", font=("Kanit", 10))
    volumn_text.pack(ipadx=10, ipady=10)
    volumn_text.place(x=40, y=255)
    volumn = tk.StringVar()
    volumn_input = ttk.Entry(page1, textvariable=volumn, width=10)
    volumn_input.pack(ipadx=5, ipady=3, expand=True)
    volumn_input.place(x=165, y=260)
    gas_state1 = ttk.Combobox(page1, values=['STP', 'customised'], width=5, state="readonly")
    gas_state1.place(x=105, y=260)
    cb_uom2 = ttk.Combobox(page1, values=['dm^3', 'cm^3'], width=5, state="readonly")
    cb_uom2.place(x=250, y=260)
    confirm_button4 = ttk.Button(page1, text='submit', command=calculate_volumn)
    confirm_button4.pack(ipadx=5, ipady=5, expand=True)
    confirm_button4.place(x=320, y=260)
    rsfv = ttk.Combobox(page1, values=['mol', 'mass', 'particle'], width=5, state="readonly")
    rsfv.place(x=425, y=260)
    output_text2 = tk.Label(page1, font=("Kanit", 10))
    output_text2.pack(ipadx=10, ipady=10)
    output_text2.place(x=495, y=255)


    # particle
    particle_text = tk.Label(page1, text="particle", font=("Kanit", 10))
    particle_text.pack(ipadx=10, ipady=10)
    particle_text.place(x=40, y=225)
    particle = tk.StringVar()
    particle_input = ttk.Entry(page1, textvariable=particle)
    particle_input.pack(ipadx=5, ipady=3, expand=True)
    particle_input.place(x=105, y=230)
    confirm_button2 = ttk.Button(page1, text='submit')
    confirm_button2.pack(ipadx=5, ipady=5, expand=True)
    confirm_button2.place(x=320, y=230)
    rsfp = ttk.Combobox(page1, values=['mol', 'mass(g)', 'volumn at STP', 'volumn at customised'], width=5,
                        state="readonly")
    rsfp.place(x=425, y=227.5)

    # gas state
    page1.vpermol = float()
    gas_state = tk.Label(page1, text="gas state", font=("Kanit", 10))
    gas_state.pack(ipadx=10, ipady=10)
    gas_state.place(x=40, y=290)
    pressure_text = tk.Label(page1, text="Pressure (P) :", font=("Kanit", 10))
    pressure_text.place(x=45, y=322.5)
    pressure_box = ttk.Entry(page1, width=10)
    pressure_box.place(x=135, y=325)
    ps_unit = ttk.Combobox(page1, values=['atm', 'Pa', 'psi', 'torr'], width=3, state="readonly")
    ps_unit.place(x=205, y=325)
    temp_text = tk.Label(page1, text="Temperature (T) :", font=("Kanit", 10))
    temp_text.place(x=275, y=322.5)
    temp_box = ttk.Entry(page1, width=10)
    temp_box.place(x=385, y=325)
    temp_unit = ttk.Combobox(page1, values=['°C', 'K', '°F'], width=3, state="readonly")
    temp_unit.place(x=455, y=325)
    checkbox = tk.StringVar()
    state_checkbox = ttk.Button(page1, command=gas_state2)
    state_checkbox.place(x=500, y=325)

    page1.mainloop()

def page2 ():

    def create ( ):

        n_reactant = int(n_of_reactant.get())
        n_product = int(n_of_product.get())

        page2.reactant_entry = [group_entry_reactant(page2 , i) for i in range(n_reactant)]
        page2.product_entry = [group_entry_product(page2 , i) for i in range(n_product)]

    def get_data ():

        n_reactant = int(n_of_reactant.get())
        n_product = int(n_of_product.get())

        data = {
            "name": "-",
            "amount": "-",
            "unit1": "-",
            "unit2": "-"
        }
        page2.reactant_data = []
        page2.product_data = []

        for i in range(n_reactant) :
            temp = dict(data)
            temp["name"] = page2.reactant_entry[i].reactant.get()
            temp["amount"] = int(page2.reactant_entry[i].rxt_dt.get())
            temp["unit1"] = page2.reactant_entry[i].rxt_unit.get()
            temp["unit2"] = page2.reactant_entry[i].rxt_type.get()
            page2.reactant_data.append(temp)

        for dt in page2.reactant_data :
            print(dt["name"] , dt["amount"] , dt["unit1"] , dt["unit2"])

        for i in range(n_product):
            temp = dict(data)
            temp["name"] = page2.product_entry[i].product.get()
            temp["amount"] = int(page2.product_entry[i].pro_dt.get())
            temp["unit1"] = page2.product_entry[i].pro_unit.get()
            temp["unit2"] = page2.product_entry[i].pro_type.get()
            page2.product_data.append(temp)

        for dt in page2.product_data:
            print(dt["name"], dt["amount"], dt["unit1"], dt["unit2"])

        reactants = [page2.reactant_data[i]['name'] for i in range(n_reactant)]
        products = [page2.product_data[i]['name'] for i in range(n_reactant)]

        print(reactants)
        print(products)

        coefficients = balance(reactants , products)

        for i in range(n_reactant) :
            page2.reactant_entry[i].bl1.delete(0, 'end')
            page2.reactant_entry[i].bl1.insert(0 , coefficients[i][0])

        for i in range(n_product) :
            page2.product_entry[i].bl2.delete(0 , 'end')
            page2.product_entry[i].bl2.insert(0 , coefficients[i + n_reactant][0])



    page2 = App()

    #-------------------------------
    page2.geometry("750x450+50+50")
    page2.resizable(False, False)
    page2.title("Analytical Helper")
    page2.iconbitmap(r'Project/Logic/443525.ico')

    # reactant
    enter_n_of_reactant = page_label(page2, text="number of reactant :", font=("Kanit", 10))
    enter_n_of_reactant.place(x=100, y=50)
    n_of_reactant = ttk.Spinbox(page2, from_=1, to=6, wrap=True, width=3)
    n_of_reactant.place(x=245, y=55)

    # product
    enter_n_of_product = page_label(page2, text="number of product :", font=("Kanit", 10))
    enter_n_of_product.place(x=325, y=50)
    n_of_product = ttk.Spinbox(page2, from_=1, to=6, wrap=True, width=3)
    n_of_product.place(x=465, y=55)

    # command
    balance_button = ttk.Button(page2, text='balance', command = get_data )
    balance_button.place(x=315, y=200)

    calculate_button = ttk.Button(page2, text='calculate')
    calculate_button.place(x=420, y=200)

    # command
    confirm_button = ttk.Button(page2, text='submit', command = create )
    confirm_button.pack(ipadx=5, ipady=5, expand=True)
    confirm_button.place(x=525, y=52.5)
    clear_button = ttk.Button(page2, text='clear')
    clear_button.place(x=605, y=52.5)

    page2.mainloop()

if __name__ == "__main__":

    app = App()

    enter_icon = Image.open(r"Project/Logic/enter_logo.png")
    resized_enter_icon = enter_icon.resize((50, 50))
    use_resized_enter_icon = ImageTk.PhotoImage(resized_enter_icon)

    enter_button_1 = page_button(app, text='ENTER PAGE I',compound=tk.LEFT , image=use_resized_enter_icon,command=page1)
    enter_button_1.pack(ipadx=4, ipady=4, expand=True)

    enter_button_2 = page_button(app, text='ENTER PAGE II', compound=tk.LEFT , image=use_resized_enter_icon,command = page2)
    enter_button_2.pack(ipadx=4, ipady=8, expand=True)

    exit_button = page_button(app, text='Farewell', compound=tk.LEFT)
    exit_button.pack(ipadx=4, ipady = 12, expand=True)


    app.mainloop()
