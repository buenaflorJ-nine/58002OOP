from tkinter import *
from tkinter import Entry


class MyWindow:

    def __init__(self,win):


    # ------------------------------------------------------ LABELS ------------------------------------------------------


        self.lbl = Label(win,text="Pressure Calculator", font="Calibri")
        self.lbl.grid(row=0, column=1, columnspan=10, sticky=N, padx=180, pady=10)

        self.lbl1 = Label(win, text= "Density (ρ) :")
        self.lbl1.grid(row=1, column=1, padx=15, pady=15, sticky="w")

        self.lbl2 = Label(win, text="Height (h) :")
        self.lbl2.grid(row=2, column=1, padx=15, pady=15, sticky="w")

        self.lbl3 = Label(win,text="Force (F) :")
        self.lbl3.grid(row=1, column=3, padx=15)

        self.lbl4 = Label(win, text= "Area (A) :")
        self.lbl4.grid(row=2, column=3, padx=15)

        self.lbl5 = Label(win, text="Answer:", font=("Arial", 18, "bold"))
        self.lbl5.grid(row=3, column=1, padx=15, pady=15, sticky="w")


    #------------------------------------------------------ TEXT ENTRIES ------------------------------------------------------


        self.__txt1 = Entry(win, bd=1)
        self.__txt1.grid(row=1, column=2, sticky="w")

        self.__txt2 = Entry(win, bd=1)
        self.__txt2.grid(row=2, column=2, sticky="w")

        self.__txt3 = Entry(win, bd=1)
        self.__txt3.grid(row=1, column=4)

        self.__txt4 = Entry(win, bd=1)
        self.__txt4.grid(row=2, column=4)

        self.__txt5 = Entry(win, width=36, justify=LEFT, font=("Arial", 18, "bold"))
        self.__txt5.grid(row=4, columnspan=10,  padx=15, sticky="w")


    #------------------------------------------------------ BUTTONS ------------------------------------------------------


        self.btn1 = Button(win, text="Calculate", bd=3, width=25, font=("Arial", 18, "bold"))
        self.btn1.grid(row=5, column=1, columnspan=10, pady=15)
        self.btn1.bind('<Button-1>', self.compute)

        self.btnclr = Button(win, text="Clear", bd=3, width=25)
        self.btnclr.grid(row=6, column=1, columnspan=10)
        self.btnclr.bind('<Button-1>', self.clear)


    # ------------------------------------------------------ FUNCTIONS ------------------------------------------------------


    def compute(self, pressure):

        if self.__txt1.get() and self.__txt3.get() or self.__txt2.get() and self.__txt4.get() or \
                self.__txt1.get() and self.__txt4.get() or self.__txt2.get() and self.__txt3.get():
            self.__txt5.delete(0, 'end')
            result = "Error"
            self.__txt5.insert(END, str(result))

        elif self.__txt1.get() and self.__txt2.get():
            self.__txt5.delete(0, 'end')
            density = int(self.__txt1.get())
            height = int(self.__txt2.get())
            result = density*height*9.8
            self.__txt5.insert(END, str(result))

        elif self.__txt3.get() and self.__txt4.get():
            self.__txt5.delete(0, 'end')
            force = int(self.__txt3.get())
            area = int(self.__txt4.get())
            result = force/area
            self.__txt5.insert(END, str(result))


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



window = Tk()
mywin = MyWindow(window)
window.geometry("500x400+10+10")
window.title("Temp Conversion")
window.configure(bg="#87CEEB")
window.mainloop()
