import tkinter
from tkinter import *


class Calculator:
    def __init__(self, win):
        self.val = ""

        self.equation = tkinter.StringVar()

        self.txt1 = Entry(win, textvariable=self.equation, font=("Arial", 25), insertwidth=4, width=11,
                          justify=RIGHT, bd=0, bg="#000000", fg="white")
        self.txt1.insert(0, "0")
        self.txt1.grid(row=0, columnspan=10, sticky=N, padx=10, pady=10)


        self.btnadd = Button(win, text="+", width=3, font=("Arial", 18, "bold"), bd=0, fg="white",
                             bg="#374FB8")
        self.btnadd.grid(row=5, column=3, pady=1)
        self.btnadd.bind('<Button-1>', self.add)


        self.btnsub = Button(win, text="-", width=3, font=("Arial", 18, "bold"), bd=0, fg="white",
                             bg="#374FB8")
        self.btnsub.grid(row=4, column=3, pady=1)
        self.btnsub.bind('<Button-1>', self.sub)


        self.btnmul = Button(win, text="*", width=3, font=("Arial", 18, "bold"), bd=0, fg="white",
                             bg="#374FB8")
        self.btnmul.grid(row=3, column=3)
        self.btnmul.bind('<Button-1>', self.mul)


        self.btndiv = Button(win, text="/", width=3, font=("Arial", 18, "bold"), bd=0, fg="white",
                             bg="#374FB8")
        self.btndiv.grid(row=6, column=3)
        self.btndiv.bind('<Button-1>', self.div)


        self.btneql = Button(win, text="=", width=3, font=("Arial", 19, "bold"), bd=0, fg="white",
                             bg="#374FB8")
        self.btneql.grid(row=6, column=1, columnspan=10, padx=10)
        self.btneql.bind('<Button-1>', self.eql)


        self.btnclr = Button(win, text="C", width=3, font=("Arial", 18, "bold"), bd=0, fg="black",
                             bg="#7b889e")
        self.btnclr.grid(column=1, row=6, pady=5 )
        self.btnclr.bind('<Button-1>', self.clr)


        self.btnN0 = Button(win, text="0", width=3, font=("Arial", 18, "bold"), bd=0, fg="white", bg="#23395d")
        self.btnN0.grid(row=6, column=0, padx=5, pady=5)
        self.btnN0.bind('<Button-1>', self.N0)


        self.btnN1 = Button(win, text="1", width=3, font=("Arial", 18, "bold"), bd=0, fg="white", bg="#23395d")
        self.btnN1.grid(row=5, column=0)
        self.btnN1.bind('<Button-1>', self.N1)


        self.btnN2 = Button(win, text="2", width=3, font=("Arial", 18, "bold"), bd=0, fg="white", bg="#23395d")
        self.btnN2.grid(row=5, column=1)
        self.btnN2.bind('<Button-1>', self.N2)


        self.btnN3 = Button(win, text="3", width=3, font=("Arial", 18, "bold"), bd=0, fg="white", bg="#23395d")
        self.btnN3.grid(row=5, column=2)
        self.btnN3.bind('<Button-1>', self.N3)


        self.btnN4 = Button(win, text="4", width=3, font=("Arial", 18, "bold"), bd=0, fg="white", bg="#23395d")
        self.btnN4.grid(row=4, column=0, padx=5, pady=5)
        self.btnN4.bind('<Button-1>', self.N4)


        self.btnN5 = Button(win, text="5", width=3, font=("Arial", 18, "bold"), bd=0, fg="white", bg="#23395d")
        self.btnN5.grid(row=4, column=1)
        self.btnN5.bind('<Button-1>', self.N5)


        self.btnN6 = Button(win, text="6", width=3, font=("Arial", 18, "bold"), bd=0, fg="white", bg="#23395d")
        self.btnN6.grid(row=4, column=2)
        self.btnN6.bind('<Button-1>', self.N6)


        self.btnN7 = Button(win, text="7", width=3, font=("Arial", 18, "bold"), bd=0, fg="white", bg="#23395d")
        self.btnN7.grid(row=3, column=0)
        self.btnN7.bind('<Button-1>', self.N7)


        self.btnN8 = Button(win, text="8", width=3, font=("Arial", 18, "bold"), bd=0, fg="white", bg="#23395d")
        self.btnN8.grid(row=3, column=1)
        self.btnN8.bind('<Button-1>', self.N8)


        self.btnN9 = Button(win, text="9", width=3, font=("Arial", 18, "bold"), bd=0, fg="white", bg="#23395d")
        self.btnN9.grid(row=3, column=2, padx=5)
        self.btnN9.bind('<Button-1>', self.N9)


    def press(self, num):
        self.val = self.val + str(num)
        self.equation.set(self.val)

    def eql(self, eql):
        try:
            self.val = self.val.replace("^", "**")
            total = str(eval(self.val))
            self.equation.set(total)
            self.val = total

        except:
            self.equation.set(" error ")
            self.val = ""

    def clr(self, clr):
        self.val = ""
        self.equation.set("0")

    def bck(self, bck):
        self.val = self.val.rstrip(self.val[-1])
        self.equation.set(self.val)

    def add(self, add):
        self.press("+")

    def sub(self, sub):
        self.press("-")

    def mul(self, mul):
        self.press("*")

    def div(self, div):
        self.press("/")

    def dec(self, dec):
        self.press(".")

    def N0(self, N0):
        self.press(0)

    def N1(self, N1):
        self.press(1)

    def N2(self, N2):
        self.press(2)

    def N3(self, N3):
        self.press(3)

    def N4(self, N4):
        self.press(4)

    def N5(self, N5):
        self.press(5)

    def N6(self, N6):
        self.press(6)

    def N7(self, N7):
        self.press(7)

    def N8(self, N8):
        self.press(8)

    def N9(self, N9):
        self.press(9)


window = Tk()
mywin = Calculator(window)


window.geometry("228x270")
window.title("Calculator")
window.eval('tk::PlaceWindow . center')
window.configure(bg="#87CEEB")

window.mainloop()