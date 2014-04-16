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
tablero = [['-', 'b', '-', 'b', '-', 'b', '-', 'b'],
           ['b', '-', 'b', '-', 'b', '-', 'b', '-'],
           ['-', 'b', '-', 'b', '-', 'b', '-', 'b'],
           ['-', '-', '-', '-', '-', '-', '-', '-'],
           ['-', '-', '-', '-', '-', '-', '-', '-'],
           ['n', '-', 'n', '-', 'n', '-', 'n', '-'],
           ['-', 'n', '-', 'n', '-', 'n', '-', 'n'],
           ['n', '-', 'n', '-', 'n', '-', 'n', '-']]

letras = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
movimientoValido = True
jugador = 'b'




#Definicion de metodos y funciones
def moValido(jugada, colorJugador):
    """
	Comprueba si la jugada es valida
	"""
    numero = 0

    if jugada[0].upper() not in letras:
        print numero
        return False

    elif jugada[2].upper() not in letras:
        print numero
        return False

    elif jugada[1] > 8 or jugada[1] < 1:
        print numero
        return False

    elif jugada[3] > 8 or jugada[3] < 1:
        print numero
        return False

    else:
        movOriRow=letras[jugada[0]]
        movOriCol=int(jugada[1])-1
        movDesRow=letras[jugada[2]]
        movDesCol=int(jugada[3])-1

        if tablero[movOriRow][movOriCol] == 0:
            return False

        ficha = tablero[movOriRow][movOriCol]

        if ficha != colorJugador:
            return False

        if (ficha == 'N') or (ficha == 'B'):

            #Logica de la dama
            return True
        else:
            #Jugada adyacente
            if ((movDesRow == movOriRow + 1 and movDesCol == movOriCol + 1) or
                    (movDesRow == movOriRow + 1 and movDesCol == movOriCol - 1) or
                    (movDesRow == movOriRow - 1 and movDesCol == movOriCol + 1) or
                    (movDesRow == movOriRow - 1 and movDesCol == movOriCol - 1)):

                fichaDestino = tablero[movDesRow][movDesCol]

                if fichaDestino == ficha:
                    return False

                return True

            else:
                return False

def moverFicha (jugada, colorJugada):
    movOriRow=letras[jugada[0]]
    movOriCol=int(jugada[1])-1
    movDesRow=letras[jugada[2]]
    movDesCol=int(jugada[3])-1

    fichaOrigen = tablero[movOriRow][movOriCol]
    fichaDestino = tablero [movDesRow][movDesCol]

    if fichaDestino == '-':
        tablero[movDesRow][movDesCol] = fichaOrigen
        tablero[movOriRow][movOriCol] = '-'

    elif fichaDestino != colorJugada:

        tablero[movOriRow][movOriCol] = '-'
        if movDesRow < movOriRow:
            if movDesCol < movOriCol:
                tablero[movDesRow - 1][movDesCol - 1] = fichaOrigen

            else:
               tablero[movDesRow - 1][movDesCol + 1] = fichaOrigen

        else:
            if movDesCol < movOriCol:
                tablero[movDesRow + 1][movDesCol - 1] = fichaOrigen

            else:
                tablero[movDesRow + 1][movDesCol + 1] = fichaOrigen


print 'Bienvenidos al juego de las damas'
print 'Comienzan las blancas'

while movimientoValido:

    movimiento = raw_input()

    if  moValido(movimiento, jugador):
        movimientoValido = True
        moverFicha(movimiento, jugador)

        print tablero[7]
        print tablero[6]
        print tablero[5]
        print tablero[4]
        print tablero[3]
        print tablero[2]
        print tablero[1]
        print tablero[0]

    else:
        movimientoValido = False
        print 'Movimiento no válido'