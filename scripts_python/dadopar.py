import os
from random import randint

#Functions
def dices() :
    status = True
    contador = 0
    acumula = 0
    os.system('clear')
    total = 0

    while status :     #while status ==> while status == True
        
        dice1 = randint(1,6)
        dice2 = randint(1,6)
        print("D1: ", dice1)
        print("D2: ", dice2)
        print("####################################################")

        
        suma = dice1 + dice2

        total += suma

        acumula +=1

        if (dice1 == dice2) :
            
            contador += 1

            if(contador == 2) :
                status = False
                print("se llego a la posicion ",acumula)
                print("la suma de las posiciones ",total) 
                print("::: Se ha llegado a 2 pares consecutivos, el juego ha terminado  :::")
        else :

            contador = 0
        
                   
        if (suma > 100) :

            status = False
            print("::: Se llego a la meta +100 :::")
            
        

#Main
dices()