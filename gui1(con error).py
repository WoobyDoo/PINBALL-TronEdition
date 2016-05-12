import tkinter
import math
from time import sleep

v = tkinter.Tk()

i1 = 0
j1 = 0
i2 = 0
j2 = 0
#k = 100
dir1 = 0
dir2 = 0

def aja():
    global canvas,poligono1,poligono2,i1,j1,i2,j2,k,texto
    i1 = i1 + 5
    j1 = j1 + 5
    i2 = i2 + 5
    j2 = j2 + 5
    pare = False
    #poligono1 = canvas.create_polygon(100+i,100+j,200+i,200+j,100+i,200+j,50+i,150+j,outline="black",fill="orange")
    #while(i<100):
    #if(i1<k):
    if((100+i1 >= 0 and 100+j1 >= 0) and (200+i1 <= 500 and 200+j1 <= 500)):
        canvas.delete(poligono1)
        poligono1 = canvas.create_oval(100+i1,100+j1,200+i1,200+j1,outline="black",fill="orange")

    if((400-i2 >= 0 and 400-j2 >= 0) and (500-i2 <= 500 and 500-j2 <= 500)):
        canvas.delete(poligono2)
        poligono2 = canvas.create_oval(400-i2,400-j2,500-i2,500-j2,outline="black",fill="red")

    distancia = math.sqrt((((150+i1)-(450-i2))**2)+(((150+j1)-(450-j2))**2))
    if(distancia <= 100):
        canvas.delete(texto)
        texto = canvas.create_text(200,200,text="SE CHOCARON!!!!!")
        pare = True
    else:
        canvas.delete(texto)

    if(not pare):
        v.after(100,aja)


    #else:
    #    k = k + 100

def aja2():
    global canvas,poligono1,j1,i1
    j1 = j1 + 5
    canvas.delete(poligono1)
    #poligono1 = canvas.create_polygon(100+i,100+j,200+i,200+j,100+i,200+j,50+i,150+j,outline="black",fill="orange")
    poligono1 = canvas.create_oval(100+i1,100+j1,200+i1,200+j1,outline="black",fill="orange")

def key(event):
    global canvas,poligono1,j1,i1
    tecla = repr(event.char)
    print("pressed" + str(tecla))
    if(tecla == "'w'"):
        j1 = j1 - 5
        canvas.delete(poligono1)
        #poligono1 = canvas.create_polygon(100+i,100+j,200+i,200+j,100+i,200+j,50+i,150+j,outline="black",fill="orange")
        poligono1 = canvas.create_oval(100+i1,100+j1,200+i1,200+j1,outline="black",fill="orange")
    if(tecla == "'a'"):
        i1 = i1 - 5
        canvas.delete(poligono1)
        #poligono1 = canvas.create_polygon(100+i,100+j,200+i,200+j,100+i,200+j,50+i,150+j,outline="black",fill="orange")
        poligono1 = canvas.create_oval(100+i1,100+j1,200+i1,200+j1,outline="black",fill="orange")
    if(tecla == "'s'"):
        j1 = j1 + 5
        canvas.delete(poligono1)
        #poligono1 = canvas.create_polygon(100+i,100+j,200+i,200+j,100+i,200+j,50+i,150+j,outline="black",fill="orange")
        poligono1 = canvas.create_oval(100+i1,100+j1,200+i1,200+j1,outline="black",fill="orange")
    if(tecla == "'d'"):
        i1 = i1 + 5
        canvas.delete(poligono1)
        #poligono1 = canvas.create_polygon(100+i,100+j,200+i,200+j,100+i,200+j,50+i,150+j,outline="black",fill="orange")
        poligono1 = canvas.create_oval(100+i1,100+j1,200+i1,200+j1,outline="black",fill="orange")

    print(tecla)
##    if(tecla == "''"):
##        j1 = j1 - 5
##        canvas.delete(poligono1)
##        #poligono1 = canvas.create_polygon(100+i,100+j,200+i,200+j,100+i,200+j,50+i,150+j,outline="black",fill="orange")
##        poligono1 = canvas.create_oval(100+i1,100+j1,200+i1,200+j1,outline="black",fill="orange")
##    if(tecla == "'a'"):
##        i1 = i1 - 5
##        canvas.delete(poligono1)
##        #poligono1 = canvas.create_polygon(100+i,100+j,200+i,200+j,100+i,200+j,50+i,150+j,outline="black",fill="orange")
##        poligono1 = canvas.create_oval(100+i1,100+j1,200+i1,200+j1,outline="black",fill="orange")
##    if(tecla == "'s'"):
##        j1 = j1 + 5
##        canvas.delete(poligono1)
##        #poligono1 = canvas.create_polygon(100+i,100+j,200+i,200+j,100+i,200+j,50+i,150+j,outline="black",fill="orange")
##        poligono1 = canvas.create_oval(100+i1,100+j1,200+i1,200+j1,outline="black",fill="orange")
##    if(tecla == "'d'"):
##        i1 = i1 + 5
##        canvas.delete(poligono1)
##        #poligono1 = canvas.create_polygon(100+i,100+j,200+i,200+j,100+i,200+j,50+i,150+j,outline="black",fill="orange")
##        poligono1 = canvas.create_oval(100+i1,100+j1,200+i1,200+j1,outline="black",fill="orange")
    

def callback(event):
    frame.focus_set()
    print("clicked at", event.x, event.y)

frame = tkinter.Frame(v, width=100, height=100)
frame.bind("<Key>", key)
##frame.bind("<Button-1>", callback)
frame.pack()

v.title("Cambio el titulo")

boton = tkinter.Button(v,text="->",command=aja)
boton2 = tkinter.Button(v,text="|\nv",command=aja2)

boton.pack()
boton2.pack()

canvas = tkinter.Canvas(v,width=500,height=500)
canvas.bind("<Key>", key)
canvas.focus_set()
canvas.pack()

#poligono1 = canvas.create_polygon(100,100,200,200,100,200,50,150,outline="black",fill="orange")
poligono1 = canvas.create_oval(100,100,200,200,outline="black",fill="orange")
poligono2 = canvas.create_oval(400,400,500,500,outline="black",fill="red")

texto = canvas.create_text(200,200,text="")


v.mainloop()
