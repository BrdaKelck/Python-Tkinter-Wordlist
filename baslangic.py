from tkinter import *
import mobil as mb

pencere = Tk()

pencere.configure(bg="#DFF7CC")

pencere.geometry("750x500+400+100")
pencere.resizable(width=False,height=False)
pencere.title("Wordlist Oluşturma")

L1 = Label(pencere,text="WordList Oluşturma",bg="#DFF7CC",fg="Black", font="17")
L1.place(x=290)

def mobil():
    pencere.destroy()
    mb.calis()
    
B1 = Button(pencere,text="Mobil İçin",bg="#85F32E",fg="white",command=mobil)
B1.place(y=100,x=100,relheight=0.2,relwidth=0.3)

def pc():
    pass

B2 = Button(pencere,text="Pc'ler İçin",bg="#85F32E",fg="white",command=pc)
B2.place(y=100,x=430,relwidth=0.3,relheight=0.2)

def cıkıs():
    pencere.destroy()

B3 = Button(pencere,text="Çıkış",bg="#85F32E",fg="white",command=cıkıs)
B3.place(x=260,y=300,relwidth=0.3,relheight=0.2)

pencere.mainloop()