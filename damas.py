# -*- coding:uft-8 -*-
_author__ = 'dcubero, ddiaz'

print ('Bienvenidos al juego de las damas!')
jugadorA = raw_input('Introduce el nombre del jugador A: ')
jugadorB = raw_input('Introduce el nombre del jugador B: ')
listaA = []
listaB = []


print("\n El primero en mover es el jugador " + jugadorA)
movimiento = 'FF'


while (movimiento != '00'):

    movimiento = raw_input('Introduce un movimiento ' + jugadorA + ': ')
    listaA.append(movimiento)

    movimiento = raw_input('Introduce un movimiento ' + jugadorB + ': ')
    listaB.append(movimiento)



print (listaA)
print (listaB)