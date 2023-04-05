# I manage to fix the wrongs of my quiz

from tkinter import *
from tkinter import Entry


class MyWindow:

    def __init__(self,win):
        self.lbl1 = Label(win,text="Input")
        self.lbl1.place(x=100,y=50)
        self.lbl2 = Label(win, text= "Celsius to Fahrenheit")
        self.lbl2.place(x=100,y=100)
        self.lbl3 = Label(win, text="Celsius to Kelvin")
        self.lbl3.place(x=100,y=150)
        self.lbl4 = Label(win,text="Fahrenheit to Celsius")
        self.lbl4.place(x=100,y=200)
        self.lbl5 = Label(win, text= "Fahrenheit to Kelvin")
        self.lbl5.place(x=100,y=250)
        self.lbl6 = Label(win, text="Kelvin to Celsius")
        self.lbl6.place(x=100,y=300)
        self.lbl7 = Label(win, text="Kelvin to Fahrenheit")
        self.lbl7.place(x=100,y=350)
        self.__txt1 = Entry(win,bd=1)
        self.__txt1.place(x=225,y=50)
        self.__txt2 = Entry(win,bd=1)
        self.__txt2.place(x=225,y=100)
        self.__txt3 = Entry(win,bd=3)
        self.__txt3.place(x=225,y=150)
        self.__txt4 = Entry(win,bd=1)
        self.__txt4.place(x=225,y=200)
        self.__txt5 = Entry(win,bd=1)
        self.__txt5.place(x=225,y=250)
        self.__txt6 = Entry(win,bd=3)
        self.__txt6.place(x=225,y=300)
        self.__txt7 = Entry(win,bd=3)
        self.__txt7.place(x=225,y=350)
        self.__btncompute = Button(win,text="Compute")
        self.__btncompute.place(x=450,y=50)
        self.btnclear = Button(win,text="Clear")
        self.btnclear.place(x=450,y=100)
        self.btnclear.bind('<Button-1>',self.clear)
        self.__btncompute.bind('<Button-1>',self.TempConver)

    def TempConver(self,cel):
        self.__txt2.delete(0, 'end')
        celsius = int(self.__txt1.get())
        result = (celsius*9/5)+32
        self.__txt2.insert(END, str(result))

        self.__txt3.delete(0, 'end')
        celsius = int(self.__txt1.get())
        result = celsius+273.15
        self.__txt3.insert(END, str(result))

        self.__txt4.delete(0, 'end')
        fahrenheit = int(self.__txt1.get())
        result = (fahrenheit-32)*5/9
        self.__txt4.insert(END, str(result))

        self.__txt5.delete(0, 'end')
        fahrenheit = int(self.__txt1.get())
        result = (1.8*fahrenheit)-459.67
        self.__txt5.insert(END, str(result))

        self.__txt6.delete(0, 'end')
        kelvin = int(self.__txt1.get())
        result = kelvin+273.15
        self.__txt6.insert(END, str(result))

        self.__txt7.delete(0, 'end')
        kelvin = int(self.__txt1.get())
        result = (kelvin+459.67)/1.8
        self.__txt7.insert(END, str(result))

    def clear(self,clear):
        self.__txt1.delete(0, 'end')
        self.__txt1.insert(END, str())
        self.__txt2.delete(0, 'end')
        self.__txt2.insert(END, str())
        self.__txt3.delete(0, 'end')
        self.__txt3.insert(END, str())
        self.__txt4.delete(0, 'end')
        self.__txt4.insert(END, str())
        self.__txt5.delete(0, 'end')
        self.__txt5.insert(END, str())
        self.__txt6.delete(0, 'end')
        self.__txt6.insert(END, str())
        self.__txt7.delete(0, 'end')
        self.__txt7.insert(END, str())

window = Tk()
mywin = MyWindow(window)
window.geometry("600x400+10+10")
window.title("Temp Conversion")
window.mainloop()
