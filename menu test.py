from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=500, height=650)

def click():
    valor = entry1.get()

label1 = Label(canvas, text="LOL")
valor = "ALGO"
entry1 = Entry(canvas, textvariable = valor)

boton = Button()

label1.grid(row = 0, column = 1)
entry1.grid(row= 0, column =1)

canvas.mainloop()
