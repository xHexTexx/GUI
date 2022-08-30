import csv
#file = open(r'\Project\periodic table.csv')
#csv_reader = csv.reader(file, delimiter=',')    
def calculate(chem_expression):
    ans = []
    molar_mass = []
    pre_element = ""
    for i in chem_expression :
        if ord(i)>=ord('A') and ord(i)<=ord('Z'):
            if pre_element!="":
                    molar_mass.append({pre_element : 1})
            pre_element = ""
        elif i=='(' :
            if pre_element!="" :
                molar_mass.append({pre_element : 1})
            pre_element = ""
            molar_mass.append('(')
        elif i==')':
            if pre_element!="":
                molar_mass.append({pre_element : 1})
            pre_element = ""
            tmp = {}
            while len(molar_mass)!=0 and molar_mass[len(molar_mass)-1]!='(':
                for k,v in molar_mass[len(molar_mass)-1].items():
                    if k in tmp:
                        tmp[k] += v
                    else:
                        tmp[k] = v
                molar_mass.pop()
            molar_mass.pop()
            molar_mass.append(tmp)
        elif not (ord(i)>=ord('a') and ord(i)<=ord('z')):
            tmp = {}
            if pre_element!="":
                molar_mass.append({pre_element : 1})
            pre_element = ""
            for k,v in molar_mass[len(molar_mass)-1].items():
                tmp[k] = v * int(i)
            molar_mass.pop()
            molar_mass.append(tmp)
        if (ord(i)>=ord('A') and ord(i)<=ord('Z')) or (ord(i)>=ord('a') and ord(i)<=ord('z')):
            pre_element += i
    
    return molar_mass

x = str(input())
print(calculate(x))