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
tablero = [['-', 'n', '-', 'n', '-', 'n', '-', 'n'],
           ['n', '-', 'n', '-', 'n', '-', 'n', '-'],
           ['-', 'n', '-', 'n', '-', 'n', '-', 'n'],
           ['-', '-', '-', '-', '-', '-', '-', '-'],
           ['-', '-', '-', '-', '-', '-', '-', '-'],
           ['b', '-', 'B', '-', 'b', '-', 'b', '-'],
           ['-', 'b', '-', 'b', '-', 'b', '-', 'b'],
           ['b', '-', 'b', '-', 'b', '-', 'b', '-']]

letras = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
movimientoValido = True
jugador = 'n'


#Definicion de metodos y funciones
def moValido(jugada, colorJugador):
    """
	Comprueba si la jugada es valida
	"""
    numero = 0

    if jugada[0].upper() not in letras:
        print numero + 1
        return False

    elif jugada[2].upper() not in letras:
        print numero + 2
        return False

    elif int (jugada[1]) > 8 or int (jugada[1]) < 1:
        print numero + 3
        return False

    elif int (jugada[3]) > 8 or int (jugada[3]) < 1:
        print numero + 4
        return False


    else:
        movOriRow=letras[jugada[0].upper()]
        movOriCol=int(jugada[1])-1
        movDesRow=letras[jugada[2].upper()]
        movDesCol=int(jugada[3])-1

        if tablero[movOriRow][movOriCol] == 0:
            print numero + 5
            return False

        ficha = tablero[movOriRow][movOriCol]

        if ficha.lower() != colorJugador:
            print numero + 6
            return False

        if (ficha == 'N') or (ficha == 'B'):
            #Logica de la dama
            numCasillas = abs (movOriCol - movDesCol)

            if numCasillas == abs (movOriRow - movDesRow):

                for i in range(numCasillas):

                    if movDesRow < movOriRow:
                        movInterRow = movOriRow - (i + 1)

                        if movDesCol < movOriCol:
                            movInterCol = movOriCol - (i + 1)

                        else:
                            movInterCol = movOriCol + (i + 1)

                    else:
                        movInterRow = movOriRow + (i + 1)

                        if movDesCol < movOriCol:
                            movInterCol = movOriCol - (i + 1)

                        else:
                            movInterCol = movOriCol + (i + 1)

                    if (tablero[movInterRow][movInterCol] != '-'):
                        return False

                return True

            else:
                return  False


        else:
            #Logica de las fichas
            #Jugada adyacente
            if ((movDesRow == movOriRow + 1 and movDesCol == movOriCol + 1) or
                    (movDesRow == movOriRow + 1 and movDesCol == movOriCol - 1) or
                    (movDesRow == movOriRow - 1 and movDesCol == movOriCol + 1) or
                    (movDesRow == movOriRow - 1 and movDesCol == movOriCol - 1)):

                fichaDestino = tablero[movDesRow][movDesCol]

                if fichaDestino == ficha:
                    print numero + 7
                    return False

                elif (fichaDestino != '-') and (movDesCol == 0 or movDesCol == 7 or
                    movDesRow == 0 or movDesRow == 7):
                    return False

                return True

            else:
                return False

def convertirDama(coordenadas, ficha):

    if (coordenadas[0] == '7') and (ficha == 'n'):
        tablero[int(coordenadas[0])][int(coordenadas[1])] = 'N'
    elif (coordenadas[0] == '0') and (ficha == 'b'):
        tablero[int(coordenadas[0])][int(coordenadas[1])] = 'B'

def moverFicha (jugada, colorJugada):
    movOriRow=letras[jugada[0].upper()]
    movOriCol=int(jugada[1])-1
    movDesRow=letras[jugada[2].upper()]
    movDesCol=int(jugada[3])-1
    coordenadasFicha = ''

    fichaOrigen = tablero[movOriRow][movOriCol]
    fichaDestino = tablero [movDesRow][movDesCol]

    if fichaDestino == '-':
        tablero[movDesRow][movDesCol] = fichaOrigen
        tablero[movOriRow][movOriCol] = '-'
        coordenadasFicha = str(movDesRow)+str(movDesCol)

    elif fichaDestino.lower() != colorJugada:


        tablero[movOriRow][movOriCol] = '-'
        tablero[movDesRow][movDesCol] = '-'
        if movDesRow < movOriRow:
            if movDesCol < movOriCol:
                tablero[movDesRow - 1][movDesCol - 1] = fichaOrigen
                coordenadasFicha = str(movDesRow - 1)+str(movDesCol - 1)

            else:
                tablero[movDesRow - 1][movDesCol + 1] = fichaOrigen
                coordenadasFicha = str(movDesRow - 1)+str(movDesCol + 1)

        else:
            if movDesCol < movOriCol:
                tablero[movDesRow + 1][movDesCol - 1] = fichaOrigen
                coordenadasFicha = str(movDesRow + 1)+str(movDesCol - 1)

            else:
                tablero[movDesRow + 1][movDesCol + 1] = fichaOrigen
                coordenadasFicha = str(movDesRow + 1)+str(movDesCol + 1)

    print 'Estas son las coordenadas de la ficha: '+coordenadasFicha
    convertirDama(coordenadasFicha, fichaOrigen)


print 'Bienvenidos al juego de las damas'

print '\n'

print tablero[7]
print tablero[6]
print tablero[5]
print tablero[4]
print tablero[3]
print tablero[2]
print tablero[1]
print tablero[0]


while movimientoValido:

    if (jugador == 'n'):
        jugador = 'b'
        movimiento = raw_input('Mueven las blancas: ')

    else:
        jugador = 'n'
        movimiento = raw_input('Mueven las negras: ')


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