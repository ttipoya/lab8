from itertools import product
from random import randint
import re
from tkinter import *
from tkinter import ttk
import sys

root = Tk()
root.title("METANIT.COM")
root.geometry("600x500")
prove = True
clicks = 0
sys.setrecursionlimit(10000)
class KOMPLEK_ZHENA:
    def __init__(self):
        self.col_el = N.get()
        self.firm = []
        self.zhena_min = mini.get()
        self.zhena_max = maxi.get()
        self.cena = []
    def firma(self):
        for i in range(1, self.col_el + 1):
            self.firm.append('K' + str(i))
        return
    def rangi(self):
        self.firma()
        global n
        n = 0
        label = ttk.Label(text="Цена каждой комплектующей:")
        label.place(x=0, y=265)
        for i in range(1, self.col_el + 1):
            self.cena.append(randint(self.zhena_min, self.zhena_max))
            label = ttk.Label(text=('K' + str(i) + '=' + str(self.cena[i - 1])))
            label.place(x=n, y=290)
            n += 50
        return


class KOMPUTERI():
    def __init__(self, firma, cena):
        self.col_el = N.get()
        self.f = firma
        self.maxi = 0
        self.maxikomb = ''
        self.kol_odinak_el = kol.get()
        self.cena = cena

    def usl(self):
        komb.rangi()
        for i in product(self.f, repeat=self.col_el):
            for m in range(0, self.col_el):
                for j in range(1, self.col_el + 1):
                    if int(i[m][-1]) == j and i.count(i[m]) <= self.kol_odinak_el:
                        self.suma = self.suma + self.cena[j - 1]
                    elif i.count(i[m]) > self.kol_odinak_el:
                        self.suma = 0
            if self.suma > self.maxi and self.suma != 0:
                self.maxi = self.suma
                self.maxikomb = i
            self.suma = 0
        label = ttk.Label(text=('Маскимальная цена: ' + str(self.maxi)))
        label.place(x=0, y=315)
        label = ttk.Label(text=('Комбинация: '))
        label.place(x=0, y=340)
        label = ttk.Label(text=self.maxikomb)
        label.place(x=75, y=340)
        return


N = IntVar()
mini = IntVar()
maxi = IntVar()
result = IntVar()
kol = IntVar()
errmsg = StringVar()


def click_button():
    global clicks
    global komb
    clicks += 1
    if clicks == 1:
        button.configure(state=DISABLED)
        komb = KOMPLEK_ZHENA()
        komp = KOMPUTERI(komb.firm, komb.cena)
        komp.usl()
    elif clicks == 0:
        button.configure(state=NORMAL)
    elif clicks > 1:
        button.configure(state=DISABLED)


def is_valid(newval):
    result = re.match("^[0-9]{0,11}$", newval) is not None
    if (not result and len(newval) <= 12 or (len(newval) == 1 and int(newval) <= 2) or (len(newval) == 1 and int(newval) > 6) or
            (len(newval) >= 1 and newval[0] == '0') or (len(newval) == 0)):
        errmsg.set("Некорректные значения")
        button.configure(state=DISABLED)
    else:
        button.configure(state=NORMAL)
        errmsg.set("")
    return result


def is_valid1(newval):
    result = re.match("^[0-9]{0,11}$", newval) is not None
    if not result and len(newval) <= 12 or (len(newval) == 1 and newval == '0') or (
            len(newval) >= 1 and newval[0] == '0') or (len(newval) == 0):
        errmsg.set("Некорректные значения")
        button.configure(state=DISABLED)
    else:
        button.configure(state=NORMAL)
        errmsg.set("")
    return result

def is_valid2(newval):
    result = re.match("^[0-9]{0,11}$", newval) is not None
    if not result and len(newval) <= 12 or (len(newval) == 1 and newval == '0') or (
            len(newval) >= 1 and newval[0] == '0') or (len(newval) == 0):
        errmsg.set("Некорректные значения")
        button.configure(state=DISABLED)
    else:
        button.configure(state=NORMAL)
        errmsg.set("")
    return result


check = (root.register(is_valid), "%P")
check1 = (root.register(is_valid1), "%P")
check2 = (root.register(is_valid2), "%P")

label = ttk.Label(text='Введите кол-во комплектующих (больше 2 и не больше 6)')
label.place(x=0, y=0)
entry = ttk.Entry(validate="key", validatecommand=check, textvariable=N)
entry.place(x=0, y=25)

label = ttk.Label(text='Введите минимальную цену(неотрицательную): ')
label.place(x=0, y=50)
entry = ttk.Entry(validate="key", validatecommand=check2, textvariable=mini)
entry.place(x=0, y=75)

label = ttk.Label(text='Введите максимальную цену(неотрицательную и больше минимальной): ')
label.place(x=0, y=100)
entry = ttk.Entry(validate="key", validatecommand=check2, textvariable=maxi)
entry.place(x=0, y=125)

label = ttk.Label(text='Введите число повторяющихся элементов не меньше 1: ')
label.place(x=0, y=150)
entry = ttk.Entry(validate="key", validatecommand=check1, textvariable=kol)
entry.place(x=0, y=175)

error_label = ttk.Label(foreground="red", textvariable=errmsg, wraplength=250)
error_label.place(x=0, y=205)

button = ttk.Button(text='ОК', command=click_button)
button.place(x=0, y=225)

root.mainloop()

