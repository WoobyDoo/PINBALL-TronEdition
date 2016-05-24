############################################################################################
# #------------------------------REFERENCIAS/REFERENCES-----------------------------------##
# #  http://stackoverflow.com/questions/27215326/tkinter-keypress-keyrelease-events       ##
# #  http://effbot.org/tkinterbook/                                                       ##
# #  http://infohost.nmt.edu/tcc/help/pubs/tkinter/tkinter.pdf                            ##
# #  https://www.youtube.com/watch?v=RJB1Ek2Ko_Y&list=PL6gx4Cwl9DGBwibXFtPtflztSNPGuIB_d  ##
# #  https://www.youtube.com/watch?v=GeX5qxerQd0                                          ##
# #---------------------------------------------------------------------------------------##
############################################################################################
from tkinter import *
import math, random, pygame, linecache
################################################
# #------------- MAIN WINDOW -----------------##
################################################
main_window = Tk()
the_name = ""
not_loaded = True
def show(ventana): ventana.deiconify()
def hide(ventana):ventana.withdraw()
def execute(f): main_window.after(200, f)
def nombre(ventana):
    global the_name
    ventana.deiconify()
    name_label.config(text=" " + entry_name.get())
    the_name += entry_name.get()
def exit(ventana):
    ventana.destroy()
main_window.config(bg="black")
main_window.geometry("500x500")
main_window.resizable(0, 0)
tron = ("tr2n", 20, "bold")
tron2 = ("tr2n", 15, "bold")
tron3 = ("tr2n", 12, "bold")
tron4 = ("tr2n", 70, "bold")
wall = PhotoImage(file="wall2.png")

canvas_main = Canvas(main_window, width=500, height=500)
canvas_main.pack(fill='none')
canvas_main.create_image(250, 250, image=wall, anchor='center')

input_label = Label(main_window, text="PLAYER NAME: ", font=tron3,  fg='black', justify=CENTER)
input_label.place(x=110, y=250)
entry_name = Entry(main_window)
entry_name.place(x=270, y=250)
player_name = entry_name.get()
b1 = Button(main_window, text=" START NEW GAME ", font=tron, command=lambda: execute(show(game_window)))
b1 = Button(main_window, text=" START NEW GAME ", font=tron, command=lambda: execute(nombre(game_window)))
b1.place(x=80, y=180)

b2 = Button(main_window, text=" MANUAL ", font=tron, command=lambda: execute(show(manual_window)))
b2.place(x=166.66, y=300)

b3 = Button(main_window, text=" LOAD GAME ", font=tron, command=lambda: get_loaded_game())
b3.place(x=140, y=350)

b4 = Button(main_window, text=" EXIT GAME ", font=tron, command=lambda: execute(exit(main_window)))
b4.place(x=142, y=400)

#####################################################
# #-------------- MANUAL WINDOW -------------------##
#####################################################
manual_window = Toplevel(main_window)
manual_window.geometry("500x500")
manual_window.title("Pinball: MANUAL")
manual_window.config(bg="black")
manual_window.resizable(0, 0)
b1_manual = Button(manual_window, text=" BACK TO MENU ", font=tron, command=lambda: execute(show(main_window)))
b1_manual = Button(manual_window, text=" BACK TO MENU ", font=tron, command=lambda: execute(hide(manual_window)))
b1_manual.place(x=100, y=430)
widget = Label(manual_window, text='Pinball: TRON Edition\n\n'
                                   'INSTRUCTIONS:\n\nThe game consist in a simple map and a ball; the objective is to make hit the ball\n'
                                   'with all the obstacles to gain points, and so, when the player reach to 2000 points it will\n'
                                   'be granted with an extra life. At the start point you will only have 3 lives, so be careful.\n'
                                   'You can shoot the ball at the start of the game but the only control you will have on it \n'
                                   'on the rest of the game is with the paddles.\n\n'
                                   'CONTROLS:\n\n You can control the paddles with the keyboard and the mouse click\n\n'
                                   '< Z > For moving the left paddle\n'
                                   '< M > For moving the right paddle\n'
                                   '< FIRE > For pushing the ball at the start of the game\n\n'
                                   'CREDITS:\n\n'
                                   'This game is entirely made wih the Tkinter GUI module for the programming language Python\n'
                                   'by Diego Felipe Galarza Chamorro, student of System & Computer Engineering for the course\n'
                                   'Introduction to Programming at the Pontifica Universidad Javeriana, Cali, Colombia, 2016\n\n\n\n'
                                   '\t\t\t\t¡Thanks for playing!', fg='white', bg='black', justify=LEFT)
widget.pack()
# #--------------GAME_MUSIC_&_SOUNDS---------------##
def play_pal():
    pygame.mixer.init()
    pygame.mixer.music.load("pallet.wav")
    pygame.mixer.music.play(1)
def play_points():
    pygame.mixer.init()
    pygame.mixer.music.load("points.wav")
    pygame.mixer.music.play(1)
def game_music():
    pygame.mixer.init()
    pygame.mixer.music.load("derezzed8bit.wav")
    pygame.mixer.music.play(-1)
# #------------------------------------------------##

########################################################
# #-------------- GAME_OVER_WINDOW -------------------##
########################################################
over_window = Toplevel(main_window)
over_window.geometry("400x400")
over_window.title("Pinball: GAME OVER")
over_window.config(bg="black")
over_window.resizable(0, 0)
over_label = Label(over_window, text=" GAME \n OVER ", font=tron4, fg='white', bg='black')
over_label.place(x=10, y=130)

########################################################
# #---------------- GAME WINDOW ----------------------##
########################################################
game_window = Toplevel(main_window)
game_window.title("Pinball: TRON Edition")
game_window.resizable(0, 0)
HEIGHT = 650
WIDTH = 500
bkimage = PhotoImage(file="bkgrid.png")
bum1 = PhotoImage(file="tred.png")
bum2 = PhotoImage(file="tgreen.png")
bum3 = PhotoImage(file="toran.png")
bum4 = PhotoImage(file="tyell.png")
canvas = Canvas(game_window, width=WIDTH, height=HEIGHT)
canvas.pack(fill='none')
canvas.create_image(230, 325, image=bkimage, anchor='center')
#game_music()
title_label = Label(game_window, text="PINBALL: TRON EDITION", font=tron2, fg='white', bg='black')
title_label.place(x=110, y=10)
player_label = Label(game_window, text="Player Name:", fg='white', bg='black')
player_label.place(x=60, y=45)
name_label = Label(game_window, text=" ", fg='white', bg='black')
name_label.place(x=135, y=45)
score_label = Label(game_window, text="Score:", fg='white', bg='black')
score_label.place(x=250, y=45)
points_label = Label(game_window, text=" ", fg='white', bg='black')
points_label.place(x=290, y=45)

lifename_label = Label(game_window, text="Life:", fg='white', bg='black')
lifename_label.place(x=380, y=45)
life_label = Label(game_window, text=" ", fg='white', bg = 'black')
life_label.place(x=410, y=45)

b1_game = Button(canvas, text="MENU", font=tron2, command=lambda: execute(show(main_window)))
b1_game = Button(canvas, text="MENU", font=tron2, command=lambda: execute(hide(game_window)))
b2_game = Button(canvas, text="SAVE", font=tron2, command=lambda: get_arch_name())
b_start = Button(canvas,text="F\nI\nR\nE", font=tron3, command=lambda: canvas.after(10, movimiento))
b1_game.place(x=0, y=620)
b2_game.place(x=0, y=10)
b_start.place(x=441, y=590)
a = 2.5
score = 0
lifes = 3

def Level():
    global a, map_borders, ob, ob2, ob3, ob4, ob5, ob6, ob7, ob8, canvas
    color = '#000E79'
    map_borders = canvas.create_polygon(475, 650, 475, 125, 425, 75, 75, 75, 25, 125, 25, 200, 74, 287.5, 25, 325, 75, 412.5,
                                     25, 450, 25, 537.5, 125, 650, 0, 650, 0, 0, 500, 0, 500, 650,outline='white', fill='black', width=2)
    ob = canvas.create_polygon(175*a, 215*a, 160*a, 240*a, 175*a, 240*a, 175*a, 180*a, 160*a, 165*a, 175*a, 130*a, 160*a, 115*a, 175*a, 80*a,
                                    175*a, 60*a, 165*a, 50*a, 175*a, 60*a, outline='white', fill = 'black', width=2)
    ob2 = canvas.create_polygon(30*a, 135*a, 42*a, 155*a, 42*a, 126*a, outline='white', fill = color, width=2)
    ob3 = canvas.create_polygon(160*a, 135*a, 148*a, 155*a, 148*a, 126*a, outline='white', fill = color, width=2)
    ob4 = canvas.create_polygon(45*a, 180*a, 30*a, 200*a, 60*a, 230*a, 45*a, 200*a, outline='white', fill=color, width=2)
    ob5 = canvas.create_polygon(145*a, 180*a, 160*a, 200*a, 130*a, 230*a, 145*a, 200*a, outline='white', fill=color, width=2)
    ob6 = canvas.create_oval(220, 122, 250, 172, outline='white', fill=color, width=2)
    ob7 = canvas.create_oval(320, 162, 350, 212, outline='white', fill=color, width=2)
    ob8 = canvas.create_oval(120, 162, 150, 212, outline='white', fill=color, width=2)

# #---------------------BALL------------------------##
def movimiento():
    global points_label, not_loaded, score, lifes
    x1, y1, x2, y2 = canvas.coords(ball["BALL"])
    x = (x1+x2)//2
    y = (y1+y2)//2
    d_bum1 = math.sqrt((x-(234+25))**2+((y+10)-(254+25))**2)
    d_bum2 = math.sqrt((x-(300+25))**2+((y+10)-(315+25))**2)
    d_bum3 = math.sqrt((x-(174+25))**2+((y+10)-(315+25))**2)

    d_obs6 = math.sqrt((x-(235+15))**2+((y+10)-(147+15))**2)
    d_obs7 = math.sqrt((x-(335+15))**2+((y+10)-(187+15))**2)
    d_obs8 = math.sqrt((x-(135+15))**2+((y+10)-(187+15))**2)

    if y <= 120 and x in range(413, 600):
        if ball["moveX"] == 0:
            ball["moveX"] = -1
        else:
            ball["moveX"] = -3
        ball["moveY"] = 0
    if x <= 24:
        if y >= 26 and y <= 198:
            ball["moveX"] = 1
#----
    if ((x >= 474  and x <= 474) and (y >= 128 and y <= 650)):
        ball["moveX"] = -1
    if ((x >= 72  and x <= 425) and (y >= 75 and y <= 75)):
        ball["moveY"] = 1
    if ((x >= 24  and x <= 68) and (y >= 250 and y <= 285)):
        ball["moveX"] = 1
    if ((x >= 25  and x <= 74) and (y >= 288 and y <= 314)):
        ball["moveX"] = 1
    if ((x >= 24  and x <= 74) and (y >= 338 and y <= 412)):
        ball["moveX"] = 1
    if ((x >= 24  and x <= 74) and (y >= 413 and y <= 440)):
        ball["moveX"] = 1
    if ((x >= 24  and x <= 24) and (y >= 450 and y <= 539)):
        ball["moveX"] = 1
    if ((x >= 24  and x <= 125) and (y >= 537 and y <= 650)):
        ball["moveX"] = 1

    if ((x >= 105  and x <= 105) and (y >= 316 and y <= 383)):
        ball["moveX"] = 1
    if ((x >= 75  and x <= 105) and (y >= 316 and y <= 337)):
        ball["moveX"] = 1
    if ((x >= 75  and x <= 105) and (y >= 337 and y <= 383)):
        ball["moveX"] = 1

    if ((x >= 114  and x <= 114) and (y >= 452 and y <= 500)):
        ball["moveX"] = 1
    if ((x >= 114  and x <= 148) and (y >= 500 and y <= 572)):
        ball["moveX"] = 1
    if ((x >= 76  and x <= 14) and (y >= 500 and y <= 574)):
        ball["moveX"] = -1
    if ((x >= 76  and x <= 114) and (y >= 500 and y <= 452)):
        ball["moveX"] = -1
#-----
    if ((x >= 438  and x <= 438) and (y >= 90 and y <= 150)):
        ball["moveX"] = -1

    if ((x >= 438  and x <= 438) and (y >= 150 and y <= 204)):
        ball["moveX"] = -1
    if ((x >= 400  and x <= 438) and (y >= 204 and y <= 288)):
        ball["moveX"] = -1

    if ((x >= 400  and x <= 438) and (y >= 288 and y <= 324)):
        ball["moveX"] = -1
    if ((x >= 400  and x <= 438) and (y >= 414 and y <= 450)):
        ball["moveX"] = -1
    if ((x >= 438  and x <= 438) and (y >= 450 and y <= 540)):
        ball["moveX"] = -1
    if ((x >= 400  and x <= 438) and (y >= 540 and y <= 598)):
        ball["moveX"] = -1


    if ((x >= 370  and x <= 370) and (y >= 317 and y <= 317)):
        ball["moveX"] = -1
    if ((x >= 370  and x <= 390) and (y >= 338 and y <= 378)):
        ball["moveX"] = -1
    if ((x >= 370  and x <= 400) and (y >= 316 and y <= 330)):
        ball["moveX"] = -1

    if ((x >= 363  and x <= 363) and (y >= 452 and y <= 500)):
        ball["moveX"] = -1
    if ((x >= 327  and x <= 363) and (y >= 500 and y <= 570)):
        ball["moveX"] = -1
    if ((x >= 327  and x <= 400) and (y >= 500 and y <= 570)):
        ball["moveX"] = 1
    if ((x >= 363  and x <= 400) and (y >= 452 and y <= 500)):
        ball["moveX"] = 1

    if d_obs6 <= 20:
        ball["moveX"] = random.choice([1, -1])
    if d_obs7 <= 20:
        ball["moveX"] = random.choice([1, -1])
    if d_obs8 <= 20:
        ball["moveX"] = random.choice([1, -1])

    if ((x >= 152  and x <= 208) and (y >= 579 and y <= 600)):
        ball["moveY"] = -2
    if ((x >= 265  and x <= 320) and (y >= 579 and y <= 600)):
        ball["moveY"] = -2
    if action == True:
        if ((x >= 152  and x <= 208) and (y >= 552 and y <= 579)):
            ball["moveY"] = -2.5
            ball["moveX"] = 1
        if ((x >= 267  and x <= 320) and (y >= 552 and y <= 579)):
            ball["moveY"] = -2.5
            ball["moveX"] = -1

    if d_bum1 <= 20:
        ball["moveX"] = random.choice([1, -1])
        #ball["moveY"] = random.choice([1, -1])
        play_points()
        score2 = int(score)
        score2 += 100
        score = str(score2)
    if d_bum2 <= 20:
        ball["moveX"] = random.choice([1, -1])
        #ball["moveY"] = random.choice([1, -1])
        play_points()
        score2 = int(score)
        score2 += 50
        score = str(score2)
    if d_bum3 <= 50:
        ball["moveX"] = random.choice([1, -1])
        #ball["moveY"] = random.choice([1, -1])
        play_points()
        score2 = int(score)
        score2 += 20
        print()
        score = str(score2)
#----Gravity adder
    if (x >= 0 and x <= 430):
        ball["moveY"] += 0.009
    if (y >= 650):
        #canvas.delete(ball["BALL"])
        #canvas.after(10, ball["BALL":canvas.create_oval(445, 565, 465, 585, outline='cyan', fill='cyan')])
        ball["moveY"] = -1
        lifes2 = int(lifes)
        lifes2 += -1
        lifes = str(lifes2)
        if lifes2 == 0:
            no_lifes()
    canvas.move(ball["BALL"], ball["moveX"], ball["moveY"])
    game_window.after(10, movimiento)
    if (4990 < int(score) < 5100) or (9990 < int(score) < 10100) or (19900 < int(score) < 20100) or (39900 < int(score) < 40100):
        lifes2 = int(lifes)
        lifes2 += 1
        lifes = str(lifes2)
    points_label.config(text=" " + str(score))
    life_label.config(text=" " + str(lifes))

ball = {"moveX": 0, "moveY": -5, "BALL": canvas.create_oval(445, 565, 465, 585, outline='cyan', fill='cyan')}
# #-------------------------------------------------##

# #-----------------END&CLOSE_GAME-----------------##
def no_lifes():
    execute(show(over_window))
    execute(hide(game_window))
    canvas.after(1000, end_game)
def end_game ():
    execute(exit(over_window))
    execute(exit(main_window))
# #------------------------------------------------##


# #-------------------OBSTACLES--------------------##
def bumpers():
    global bump_1, bump_2, bump_3, canvas
    bump_1 = canvas.create_oval(210, 230, 260, 280, outline = 'black', fill = 'black')
    bump_2 = canvas.create_oval(275, 290, 325, 340, outline = 'black', fill = 'black')
    bump_3 = canvas.create_oval(150, 290, 200, 340, outline = 'black', fill = 'black')
# #------------------------------------------------##

# #------------------FLIPPER 1-----------------------##
def pal1():
    global canvas, paleta1, a
    paleta1 = canvas.create_polygon(150, 575, 210, 600, 195, 605, outline = 'red', fill = 'red', width = 2)
def pal11():
    global canvas, paleta1, a
    paleta1 = canvas.create_polygon(150, 575, 210, 550, 195, 570, outline = 'red', fill = 'red', width = 2)
def pal1update():
    global canvas, paleta1, a
    canvas.delete(paleta1)
    pal1()
# #-------------------------------------------------##
5
# #-------------------FLIPPER 2----------------------##
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
# #-------------------------------------------------##

def motion(event):
    print("Mouse position: (%s %s)" % (event.x, event.y))
canvas.bind('<Motion>', motion)

# #--------------------KEYS-------------------------##
def key_press(event):
    global canvas, paleta1, paleta2, a, ball, action
    key = repr(event.char)
    print("pressed" + str(key))
    action = False
    if key == "'z'":
        canvas.delete(paleta1)
        game_window.after(0, pal11)
        game_window.after(200, pal1update)
        action = True
        play_pal()

    if key == "'m'":
        canvas.delete(paleta2)
        game_window.after(0, pal22)
        game_window.after(200, pal2update)
        action = True
        play_pal()
    if key == "'b'":
        game_window.after(100, movimiento)
# #------------------------------------------------##


# #------------------SAVE_GAME---------------------##
def get_arch_name():
    global arch_name
    arch_name = "Pinball_Slot1"
    save_game()
    game_window.after(600, execute(exit(main_window)))

def save_game():
    global lifes, score, the_name
    arch_def = arch_name
    saved_slot = open(arch_def+".txt", "w")
    pl_name = str(the_name)
    points = str(score)
    life = str(lifes)
    saved_slot.write(pl_name + '\n')
    saved_slot.write(points + '\n')
    saved_slot.write(life + '\n')
    saved_slot.close()
# #------------------------------------------------##


# #------------------LOAD_GAME---------------------##
def get_loaded_game():
    load_game()
    main_window.after(500, execute((show(game_window))))
def load_game():
    global score, lifes
    arch_def = "Pinball_Slot1"
    saved_slot = open(arch_def+".txt", "r")
    name_out = saved_slot.readline()
    score = saved_slot.readline()
    lifes = saved_slot.readline()
    name_label.config(text=" " + name_out)
    points_label.config(text=" " + score)
    life_label.config(text=" " + lifes)
# #------------------------------------------------##


game_window.bind("<KeyPress>", key_press)
game_window.bind('<Escape>', lambda event: event.widget.quit())
game_window.bind_all()
game_window.focus_set()

# #---------------OBJECT UPDATE-------------------##
pal1()
pal2()
Level()
bumpers()
canvas.create_image(205, 228, image=bum1, anchor='nw')
canvas.create_image(270, 288, image=bum2, anchor='nw')
canvas.create_image(145, 288, image=bum3, anchor='nw')
# #-----------------------------------------------##

# #--------------LOOP&WITHDRAW-----------------##
manual_window.withdraw()
game_window.withdraw()
over_window.withdraw()
main_window.mainloop()
# #--------------------------------------------##
