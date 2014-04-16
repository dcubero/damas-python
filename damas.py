#!/usr/bin/python
#coding=utf-8
#
#Titulo:
#Damas-python
#
#Autores:
#Diego Cubero
#Daniel Díaz
#
#Descripcion:
#Juego de las damas desarrollando en python


#Definicion de variables
tablero = [[0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0], [2, 0, 2, 0, 2, 0, 2, 0], [0, 2, 0, 2, 0, 2, 0, 2], [2, 0, 2, 0, 2, 0, 2, 0]]

letras = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
movimientoValido = True




#Definicion de metodos y funciones
def moValido(jugada):
    """
	Comprueba si la jugada es valida
	"""

    if jugada[0].upper() not in letras:
        return False

    elif jugada[2].upper() not in letras:
        return False

    elif jugada[1] > 8 or jugada[1] < 1:
        return False

    elif jugada[3] > 8 or jugada[3] < 1:
        return False

    else:
        movOriRow=letras[jug[0]]
        movOriCol=int(jug[1])-1
        movDesRow=letras[jug[2]]
        movDesCol=int(jug[3])-1

        ficha = tablero[movOriRow][movOriCol]

        if (ficha.tipo == "dama" ):

            return True
        else:
            #Jugada adyacente
            if ((movDesRow == movOriRow + 1 and movDesCol == movOriCol + 1) or
                    (movDesRow == movOriRow + 1 and movDesCol == movOriCol - 1) or
                    (movDesRow == movOriRow - 1 and movDesCol == movOriCol + 1) or
                    (movDesRow == movOriRow - 1 and movDesCol == movOriCol - 1)):
                return True

            else:
                return False





print 'Bienvenidos al juego de las damas'

while movimientoValido:
    movimiento = raw_input()



    movimientoValido = moValido(movimiento)

    print tablero[7]
    print tablero[6]
    print tablero[5]
    print tablero[4]
    print tablero[3]
    print tablero[2]
    print tablero[1]
    print tablero[0]



#Definicion de clases
class Ficha:
    color = ''
    posicion = 0
    tipo = ''


    def __init__(self, color, posicion, tipo):
        self.color = color
        self.posicion = posicion
        self.tipo = tipo


    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def getPosicion(self):
        return self.posicion

    def setPosicion(self, poscion):
        self.posicion = poscion

    def getTipo(self):
        return self.tipo