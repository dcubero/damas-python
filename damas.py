#!/usr/bin/python
#coding=utf-8
#
#Titulo:
#Damas-python
#
#Autor:
#dcubero
#diaz
#
#Descripcion:
#Juego de las damas desarrollando en python


print ('Bienvenidos al juego de las damas!')
jugadorA = raw_input('Introduce el nombre del jugador A: ')
jugadorB = raw_input('Introduce el nombre del jugador B: ')
listaA = []
listaB = []


print("\n El primero en mover es el jugador " + jugadorA)
movimiento = 'FF'


while movimiento != '00':

    movimiento = raw_input('Introduce un movimiento ' + jugadorA + ': ')
    listaA.append(movimiento)

    movimiento = raw_input('Introduce un movimiento ' + jugadorB + ': ')
    listaB.append(movimiento)


def convertirMovimientos(mov):
    letras={"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7}




print (listaA)
print (listaB)

