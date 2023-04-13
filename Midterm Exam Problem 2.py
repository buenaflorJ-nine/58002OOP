from tkinter import *
from tkinter import Entry


class MyWindow:

    def __init__(self,win):
        self.lbl1 = Label(win,text="My Full Name", foreground="Red", font="Verdana")
        self.lbl1.place(x=225,y=50)
        self.lbl2 = Label(win, text= "Enter Given Name:", foreground="Red")
        self.lbl2.place(x=100,y=100)
        self.lbl3 = Label(win, text="Enter Middle Name", foreground="Red")
        self.lbl3.place(x=100,y=150)
        self.lbl4 = Label(win,text=" Enter Last name", foreground="Red")
        self.lbl4.place(x=100,y=200)
        self.lbl5 = Label(win, text= "My Full name is:", foreground="Red")
        self.lbl5.place(x=100,y=250)
        self.__txt1 = Entry(win,bd=2)
        self.__txt1.place(x=300,y=100)
        self.__txt2 = Entry(win,bd=2)
        self.__txt2.place(x=300,y=150)
        self.__txt3 = Entry(win,bd=2)
        self.__txt3.place(x=300,y=200)
        self.__txt4 = Entry(win,bd=2, foreground="Red", width=40)
        self.__txt4.place(x=300,y=250)
        self.__btnFullname = Button(win,text="Show Full Name", width=20)
        self.__btnFullname.place(x=215,y=300)
        self.__btnFullname.bind('<Button-1>',self.FullName)
        self.btnclear = Button(win, text="Clear All")
        self.btnclear = Button(win, text="Clear All", width=20)
        self.btnclear.place(x=215, y=350)
        self.btnclear.bind('<Button-1>', self.clear)

    def FullName(self,cel):
        givenN = self.__txt1.get()
        midN = self.__txt2.get()
        lastN = self.__txt3.get()
        full_name = f"{lastN} {givenN} {midN}"
        self.__txt4.insert(END, str(full_name))

    def clear(self, clear):
        self.__txt1.delete(0, 'end')
        self.__txt1.insert(END, str())
        self.__txt2.delete(0, 'end')
        self.__txt2.insert(END, str())
        self.__txt3.delete(0, 'end')
        self.__txt3.insert(END, str())
        self.__txt4.delete(0, 'end')
        self.__txt4.insert(END, str())



window = Tk()
mywin = MyWindow(window)
window.geometry("600x400+10+10")
window.title("Midterm Exam Problem 2")
window.mainloop()