import random
import math

def mazoInicial(mazo):
     if(len(mazo)<44):
         mazoInicial(mazo+list(range(1,12)))
     print (mazo)
     return mazo
and math.floor(random.randint(1,5))>1

def comprobarAs(mazo,i):
    if(i<len(mazo)):
        if(mazo[0]==1):
            print("su As va ha ser un 11")
            mazo.append(11)
            mazo.pop(0)
            return mazo
        else:
            mazo.append(mazo[0])
            mazo.pop(0)
            return comprobarAs(mazo,i+1)

def comprobar(mazo):    
    if(mazo==[]):
        return 0
    else:

        return mazo[0] + comprobar(mazo[1:])
            
def baraja(mazo,mazoBase,rnd,t):
    if(len(mazo)<=52):
        if(len(mazoBase)>=1 and t>1):
            mazo.append(mazoBase[rnd])
            mazoBase.pop(rnd)            
            baraja(mazo,mazoBase,math.floor(random.randrange(0,t-1)),t-1)
    return mazo
                   
                    
def jugador(baraja, mJugador):
    #print("baraja: ",baraja)
    print("Mano del Jugador: ", mJugador)    
    if(len(mJugador)<2):
        jugador(baraja[2:],mJugador+[baraja[0]]+[baraja[1]])
    else:
        if(mJugador.count(11)<1 and comprobar(mJugador)<11):
            comprobarAs(mJugador,0)
            print("Mano del Jugador: ", mJugador)
        if(comprobar(mJugador)<=21):
            if(comprobar(mJugador)==21):
                print("Ganaste")                
            elif(input("Quieres una carta?  ")==('s' or 'S')):            
                print(len(mJugador))
                jugador(baraja[1:],mJugador+[baraja[0]])                
            else:
                print("Mano del Jugador: ", mJugador)
                print(comprobar(mJugador))
                computador(baraja, [], mJugador)
        else:
            if(mJugador.count(11)==1):
                mJugador.pop(mJugador.index(11))
                mJugador.append(1)
                jugador(baraja,mJugador)   
            print(comprobar(mJugador))
            print("Perdiste")

def computador(baraja, mPC, mJugador):
    print("Mano del PC:  ", mPC)
    if(len(mPC)<2):
        computador(baraja[2:],mPC+[baraja[0]]+[baraja[1]],mJugador)
    else:
        if(mPC.count(11)<1 and comprobar(mPC)<11):
            comprobarAs(mPC,0)
            print("Mano de la Maquina: ", mPC)
        if(comprobar(mPC)<=21):            
            if(comprobar(mPC)==21):
                print("Gana la Maquina!")
            elif(comprobar(mPC)<=comprobar(mJugador)):
                computador(baraja[1:], mPC+[baraja[0]],mJugador)
            else:
                print("Mano de la Maquina: ", mPC)
                if(comprobar(mPC)>comprobar(mJugador)):
                    print("Perdiste")
        else:
            if(mPC.count(11)==1):
                mPC.pop(mPC.index(11))
                mPC.append(1)
                computador(baraja,mPC)
            print(comprobar(mPC))
            print("Ganaste")


jugador(baraja([],[1,2,3,4,5,6,7,8,9,10,10,10,10,1,2,3,4,5,6,7,8,9,10,10,10,10,1,2,3,4,5,6,7,8,
                  9,10,10,10,10,1,2,3,4,5,6,7,8,9,10,10,10,10],
                  math.floor(random.randrange(0,52)),52),[])

raw_input("")