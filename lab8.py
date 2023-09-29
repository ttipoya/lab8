from itertools import product
from random import randint
import re
from tkinter import *
from tkinter import ttk
import sys

root = Tk()
root.title("ВАРИАНТ 28.COM")
root.geometry("600x500")
prove = True
clicks = 0
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
wh = (w//2)-300
hh = (h//2)-300
root.geometry(f"600x500+{wh}+{hh}")
class KOMUTER:
    def __init__(self,col,nugh,mini,maxi):
        self.col = col.get()
        self.nugh = nugh.get()
        self.mini = mini.get()
        self.maxi = maxi.get()
        self.cena = []
        self.f = []
        self.suma = 0
        self.maxis = 0
        self.maxikomb = ''
    def FIRMA_KOMPLEKT(self):
        for i in range(1,self.col+1):
            self.f.append('K'+str(i))
        return self.f
    def CENA_KOMPLEKT(self):
        for i in range(1,self.col+1):
            if self.mini < self.maxi:
                self.cena.append(randint(self.mini,self.maxi))
            else:
                self.cena.append(randint(self.maxi, self.mini))
    def VAR_COMPLEK(self):
        for i in product(self.f, repeat=self.col):
            #print(i)
            pass
    def MAX_VAR_PO_CHENA(self):
        for i in product(self.f, repeat=self.col):
            for m in range(0, self.col):
                for j in range(1, self.col + 1):
                    if int(i[m][-1]) == j and i.count(i[m]) <= self.nugh:
                        self.suma = self.suma + self.cena[j - 1]
                    elif i.count(i[m]) > self.nugh:
                        self.suma = 0
            if self.suma > self.maxis and self.suma != 0:
                self.maxis = self.suma
                self.maxikomb = i
            self.suma = 0


col = IntVar()
mini = IntVar()
maxi = IntVar()
result = IntVar()
errmsg = StringVar()
nugh = IntVar()

def click_button():
    global clicks
    clicks += 1
    n = 0
    if clicks == 1:
        button.configure(state=DISABLED)
        kam = KOMUTER(col,nugh,mini,maxi)
        kam.FIRMA_KOMPLEKT()
        kam.CENA_KOMPLEKT()
        kam.MAX_VAR_PO_CHENA()
        label = ttk.Label(text="Цена каждой комплектующей:")
        label.place(x=0, y=265)
        for i in range(0,col.get()):
            label = ttk.Label(text=((kam.f[i]) +"-" + str(kam.cena[i])))
            label.place(x=n, y=290)
            n += 50
        label = ttk.Label(text=('Маскимальная цена: ' + str(kam.maxis)))
        label.place(x=0, y=315)
        label = ttk.Label(text=('Комбинация: '))
        label.place(x=0, y=340)
        label = ttk.Label(text=kam.maxikomb)
        label.place(x=75, y=340)
    elif clicks == 0:
        button.configure(state=NORMAL)
    elif clicks > 1:
        button.configure(state=DISABLED)

def coli(newval):
    result = re.match("^[0-9]{0,11}$", newval) is not None
    if (not result and len(newval) <= 12 or (len(newval) == 1 and int(newval) <= 2) or (len(newval) == 1 and int(newval) > 6) or
            (len(newval) >= 1 and newval[0] == '0') or (len(newval) == 0)):
        errmsg.set("Некорректные значения")
        button.configure(state=DISABLED)
    else:
        button.configure(state=NORMAL)
        errmsg.set("")
    return result


def nughi(newval):
    result = re.match("^[0-9]{0,11}$", newval) is not None
    if not result and len(newval) <= 12 or (len(newval) == 1 and newval == '0') or (
            len(newval) >= 1 and newval[0] == '0') or (len(newval) == 0) or (len(newval) == 1 and newval == '1'):
        errmsg.set("Некорректные значения")
        button.configure(state=DISABLED)
    else:
        button.configure(state=NORMAL)
        errmsg.set("")
    return result
def chena(newval):
    result = re.match("^[0-9]{0,11}$", newval) is not None
    if not result and len(newval) <= 12 or (len(newval) == 1 and newval == '0') or (
            len(newval) >= 1 and newval[0] == '0') or (len(newval) == 0):
        errmsg.set("Некорректные значения")
        button.configure(state=DISABLED)
    else:
        button.configure(state=NORMAL)
        errmsg.set("")
    return result

check1 = (root.register(coli), "%P")
check2 = (root.register(nughi), "%P")
check3 = (root.register(chena), "%P")

label = ttk.Label(text='Введите кол-во комплектующих (от 2 до 6)')
label.place(x=0, y=0)
entry = ttk.Entry(validate="key", validatecommand=check1, textvariable=col)
entry.place(x=0, y=25)

label = ttk.Label(text='Введите первую границу цены(неотрицательную): ')
label.place(x=0, y=50)
entry = ttk.Entry(validate="key", validatecommand=check3, textvariable=mini)
entry.place(x=0, y=75)

label = ttk.Label(text='Введите вторую границу цены(неотрицательную): ')
label.place(x=0, y=100)
entry = ttk.Entry(validate="key", validatecommand=check3, textvariable=maxi)
entry.place(x=0, y=125)

label = ttk.Label(text='Введите число повторяющихся элементов не меньше 1: ')
label.place(x=0, y=150)
entry = ttk.Entry(validate="key", validatecommand=check2, textvariable=nugh)
entry.place(x=0, y=175)

error_label = ttk.Label(foreground="red", textvariable=errmsg, wraplength=250)
error_label.place(x=0, y=205)

button = ttk.Button(text='ОК', command=click_button)
button.place(x=0, y=225)

root.mainloop()

