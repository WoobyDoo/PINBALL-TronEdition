from tkinter import *
import random
import os

main_window = Tk()
def show(ventana): ventana.deiconify()
def hide(ventana):ventana.withdraw()
def execute(f): main_window.after(200,f)

main_window.config(bg="black")
main_window.geometry("500x500")

b1=Button(main_window,text=" START GAME ",command=lambda: execute(show(game_window)))
b1.place(x= 166.66,y= 100)

b2=Button(main_window,text=" MANUAL ",command=lambda: execute(show(manual_window)))
b2.place(x= 166.66,y= 150)

b3=Button(main_window,text=" EXIT GAME ",command=lambda: execute(hide(main_window)))
b3.place(x= 166.66, y= 200)

####################################################
################# MANUAL WINDOW #####################
manual_window = Toplevel(main_window)
manual_window.geometry("500x500")
manual_window.title("Pinball: MANUAL")
manual_window.config(bg="black")
manual_window.resizable(0,0)
b1_manual=Button(manual_window,text=" BACK TO MENU ",command=lambda: execute(show(main_window)))
b1_manual=Button(manual_window,text=" BACK TO MENU ",command=lambda: execute(hide(manual_window)))
b1_manual.place(x= 195,y= 450)
widget = Label(manual_window, text='Pinball: TRON Edition\n\n'
                                   'INSTRUCTIONS:\n\nThe game consist in a simple map and a ball; the objective is to make hit the ball\n'
                                   'with all the obstacles to gain points, and so, when the player reach to 2000 points it will\n'
                                   'be granted with an extra life. At the start point you will only have 3 lives, so be careful.\n'
                                   'You can shoot the ball at the start of the game but the only control you will have on it \n'
                                   'on the rest of the game is with the paddles.\n\n'
                                   'CONTROLS:\n\n You can control the paddles with the keyboard and the mouse click\n\n'
                                   '< Z > For moving the left paddle\n'
                                   '< M > For moving the right paddle\n'
                                   '< START > For pushing the ball at the start of the game\n\n'
                                   'CREDITS:\n\n'
                                   'This game is entirely made wih the Tkinter GUI module for the programming language Python\n'
                                   'by Diego Felipe Galarza Chamorro, student of System & Computer Engineering for the course\n'
                                   'Introduction to Programming at the Pontifica Universidad Javeriana, Cali, Colombia, 2016\n\n\n\n'
                                   '\t\t\t\t¡Thanks for playing!', fg='white', bg='black', justify=LEFT)
widget.pack()


#####################################################
#################GAME WINDOW#########################

game_window = Toplevel(main_window)
game_window.title("Pinball: TRON Edition")                           #Game title
game_window.resizable(0,0)

bkimage = PhotoImage(file = "hexbg.png")
canvas = Canvas(game_window, width=500, height=650)                  #Canvas size 600x700
canvas.pack(fill = 'none')
canvas.create_image(-10,0,image = bkimage, anchor='center')
b1_game=Button(canvas,text="BACK TO MENU",command=lambda: execute(show(main_window)))
b1_game=Button(canvas,text="BACK TO MENU",command=lambda: execute(hide(game_window)))
b1_game.place(x= 0,y= 620)

a = 2.5

# def palsound():
#     os.system("pallet.wav")
# def points():
#     os.system("PINBALL\points.wav")


def Level():
    global a,map_borders, ob, ob2, ob3, ob4, ob5, ob6, ob7, ob8, canvas


    color = '#000E79' ##000E79
    map_borders = canvas.create_polygon(190*a, 260*a, 190*a, 50*a, 170*a, 30*a, 30*a, 30*a, 10*a, 50*a, 10*a, 80*a, 30*a, 115*a,10*a, 130*a, 30*a, 165*a,
                                     10*a, 180*a, 10*a, 215*a, 50*a, 260*a, 0*a, 260*a, 0*a, 0*a,200*a, 0*a, 200*a, 260*a,outline = 'white', fill= 'black', width = 2 )
    ob = canvas.create_polygon(175*a, 215*a, 160*a, 240*a, 175*a, 240*a, 175*a, 180*a, 160*a, 165*a, 175*a, 130*a, 160*a, 115*a, 175*a, 80*a,
                                    175*a, 60*a, 165*a, 50*a, 175*a, 60*a, outline = 'white', fill = 'black', width = 2)
    ob2 = canvas.create_polygon(30*a, 135*a, 42*a, 155*a, 42*a, 126*a, outline= 'white', fill = color, width = 2)
    ob3 = canvas.create_polygon(160*a, 135*a, 148*a, 155*a, 148*a, 126*a, outline= 'white', fill = color, width = 2)
    ob4 = canvas.create_polygon(45*a, 180*a, 30*a, 200*a, 60*a, 230*a, 45*a, 200*a, outline= 'white', fill = color, width = 2)
    ob5 = canvas.create_polygon(145*a, 180*a, 160*a, 200*a, 130*a, 230*a, 145*a, 200*a, outline= 'white', fill = color, width = 2)
    ob6 = canvas.create_polygon(95*a, 50*a, 105*a, 50*a, 105*a, 70*a, 95*a, 70*a, outline= 'white', fill = color, width = 2, smooth = 1)
    ob7 = canvas.create_polygon(125*a, 60*a, 135*a, 60*a, 135*a, 80*a, 125*a, 80*a, outline= 'white', fill = color, width = 2, smooth = 1)
    ob8 = canvas.create_polygon(65*a, 60*a, 75*a, 60*a, 75*a, 80*a, 65*a, 80*a, outline= 'white', fill = color, width = 2, smooth = 1)

##------------------PALETA 1-----------------------##
def pal1():
    global canvas, paleta1, a
    paleta1 = canvas.create_polygon(60*a, 230*a, 84*a, 240*a, 78*a, 242*a, outline = 'red', fill = 'red', width = 2)

def pal11():
    global canvas, paleta1, a
    paleta1 = canvas.create_polygon(60*a, 230*a, 84*a, 220*a, 78*a, 228*a, outline = 'red', fill = 'red', width = 2)

def pal1update():
    global canvas, paleta1, a
    canvas.delete(paleta1)
    pal1()
##-------------------------------------------------##


##-------------------PALETA 2----------------------##
def pal2():
    global canvas, paleta2, a
    paleta2 = canvas.create_polygon(130*a, 230*a, 106*a, 240*a, 112*a, 242*a, outline = 'red', fill = 'red', width = 2)

def pal22():
    global canvas, paleta2, a
    paleta2 = canvas.create_polygon(130*a, 230*a, 106*a, 220*a, 112*a, 228*a, outline = 'red', fill = 'red', width = 2)

def pal2update():
    global canvas, paleta2, a
    canvas.delete(paleta2)
    pal2()
##-------------------------------------------------##




def Ball():
    global canvas, a, ball, vel
    vel = [-1,-1]
    ball = canvas.create_oval(20, 20, 0, 0, outline = 'cyan', fill = 'cyan')
    canvas.move(ball, 178.2*a, 228*a)

def key_press(event):
    global canvas,paleta1, paleta2, a, ball, vel
    key = repr(event.char)
    print("pressed" + str(key))

    if key == "'z'":
        canvas.delete(paleta1)
        canvas.after(0,pal11)
        canvas.after(300,pal1update)

    if key == "'m'":
        canvas.delete(paleta2)
        canvas.after(0, pal22)
        canvas.after(300, pal2update)

    if key == "'a'":
        i=1
        while i<100:
            canvas.move(ball,(vel[0]*0.5), vel[1]*0.5)

            i+=1


canvas.bind_all("<Key>", key_press)
canvas.bind_all('<Escape>', lambda event: event.widget.quit())
canvas.focus_set()
canvas.pack()



level = Level()
Ball()
pal1()
pal2()
#bump = Bump(canvas)

manual_window.withdraw()
game_window.withdraw()
main_window.mainloop()
