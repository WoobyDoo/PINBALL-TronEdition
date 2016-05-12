name=input("Ingrese el nombre de la partida a guardar : ")
archi = open(name+".txt","w")
nombre="jugador"
puntos="1000"
vidas="2"
archi.write(nombre+'\n')
archi.write(puntos+'\n')
archi.write(vidas+'\n')
archi.close()
