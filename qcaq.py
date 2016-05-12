from tkinter import *

root = Tk()


def click():
    valor = entry1.get()

label1 = Label(root, text="")
valor = ""
entry1 = Entry(root, textvariable = valor)

boton = Button()

label1.grid(row = 0, column = 1)
entry1.grid(row= 0, column =2)

root.mainloop()

##############################################################
#           PARA EJECUTAR UN SONIDO

from tkinter import *
from winsound import *

root = Tk() # create tkinter window

play = lambda: PlaySound('Sound.wav', SND_FILENAME)
button = Button(root, text = 'Play', command = play)

button.pack()
root.mainloop()
