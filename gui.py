import tkinter

v = tkinter.Tk()

i = 0
j = 0

def aja():
    global canvas,poligono1,i,j
    i = i + 5
    canvas.delete(poligono1)
    poligono1 = canvas.create_polygon(100+i,100+j,200+i,200+j,100+i,200+j,50+i,150+j,outline="black",fill="orange")

def aja2():
    global canvas,poligono1,j,i
    j = j + 5
    canvas.delete(poligono1)
    poligono1 = canvas.create_polygon(100+i,100+j,200+i,200+j,100+i,200+j,50+i,150+j,outline="black",fill="orange")


def key(event):
    global canvas,poligono1,j,i
    tecla = repr(event.char)
    print("pressed" + str(tecla))
    if(tecla == "'w'"):
        j = j - 5
        canvas.delete(poligono1)
        poligono1 = canvas.create_polygon(100+i,100+j,200+i,200+j,100+i,200+j,50+i,150+j,outline="black",fill="orange")
    if(tecla == "'a'"):
        i = i - 5
        canvas.delete(poligono1)
        poligono1 = canvas.create_polygon(100+i,100+j,200+i,200+j,100+i,200+j,50+i,150+j,outline="black",fill="orange")
    if(tecla == "'s'"):
        j = j + 5
        canvas.delete(poligono1)
        poligono1 = canvas.create_polygon(100+i,100+j,200+i,200+j,100+i,200+j,50+i,150+j,outline="black",fill="orange")
    if(tecla == "'d'"):
        i = i + 5
        canvas.delete(poligono1)
        poligono1 = canvas.create_polygon(100+i,100+j,200+i,200+j,100+i,200+j,50+i,150+j,outline="black",fill="orange")

v.title("Cambio el titulo")

canvas = tkinter.Canvas(v,width=500,height=500)
canvas.bind("<Key>", key)
canvas.focus_set()
canvas.pack()

poligono1 = canvas.create_polygon(100,100,200,200,100,200,50,150,outline="black",fill="orange")

v.mainloop()
