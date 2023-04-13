import math
from tkinter import *
from tkinter import Entry


class MyWindow:

    def __init__(self,win):
        self.lbl1 = Label(win,text="Radius/Diameter")
        self.lbl1.place(x=100,y=50)
        self.lbl2 = Label(win, text= "Perimeter")
        self.lbl2.place(x=100,y=100)
        self.lbl3 = Label(win, text="Area")
        self.lbl3.place(x=100, y=150)
        self.__txt1 = Entry(win,bd=1)
        self.__txt1.place(x=225,y=50)
        self.__txt2 = Entry(win,bd=1)
        self.__txt2.place(x=225,y=100)
        self.__txt3 = Entry(win,bd=3)
        self.__txt3.place(x=225,y=150)
        self.__btncompute = Button(win,text="Compute")
        self.__btncompute.place(x=100,y=200)
        self.__btncompute.bind('<Button-1>',self.Compute)

    def Compute(self,cel):
        self.__txt2.delete(0, 'end')
        perimeter = int(self.__txt1.get())
        result = 2*math.pi*perimeter
        self.__txt2.insert(END, str(result))

        self.__txt3.delete(0, 'end')
        radius = int(self.__txt1.get())
        result = (radius**2) * math.pi
        self.__txt3.insert(END, str(result))

window = Tk()
mywin = MyWindow(window)
window.geometry("600x400+10+10")
window.title("Temp Conversion")
window.mainloop()