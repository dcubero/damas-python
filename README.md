Damas Python
============

Juego de las damas desarrollado en python.

Las damas se juegan en un tablero de 8x8, y cada jugador dispone al inicio de 12 piezas (peones) en la disposición que se muestra en la figura. Para indicar un movimiento, se utiliza una notación en la que las filas se nombran con letras y las columnas con números.
El movimiento se indica proporcionando la casilla inicial y la final. Por ejemplo, el movimiento indicado por la flecha roja en la figura se indicaría como C4D5

La aplicación deberá comprobar que se introduce una jugada válida (en caso contrario indicará que es errónea y volverá a pedirla), y mostrará el estado del tablero tras la jugada.

Las reglas de las damas españolas son las siguientes:

1. Las piezas sólo se mueven en diagonal (es decir, sólo van a poder estar sobre casillas de fondo blanco).
2. Los peones sólo pueden moverse a una posición adyacente y que sea una casilla libre, con la siguiente excepción:
3. Si la casilla a la que se va a mover está ocupada por una pieza contraria, y puede "saltar" sobre ella (al saltar, siguiendo la misma dirección diagonal, encuentra una casilla libre):
4. Entonces obligatoriamente salta sobre la pieza, la cuál desaparece del tablero (es una pieza "comida"). Si en esa nueva posición puede "comer" a una o más de una piezas contrarias, se repite el paso 4.
5. Si en la situación anterior (4) existen varias piezas contrarias que pueden ser "comidas", se debe elegir obligatoriamente la secuencia de movimientos que maximize el número de piezas "comidas" en total.
6. Si existieran varias secuencias con el mismo número de piezas comidas, se elige (aleatoriamente) cualquiera de ellas.
7. Si un peón negro alcanza la fila H o un peón blanco alcanza la fila A, promociona a reina.
8. Una reina puede moverse diagonalmente cualquier número de casillas mientras en ese 
movimiento diagonal recorra sólo casillas vacías. 
9. Respecto a comer piezas una reina se comporta exactamente igual que un peón, salvo por 
el hecho de que puede hacer recorridos diagonales de cualquier longitud (siempre por casillas vacías) 
10. Gana la partida quien se "come" todas las piezas del contrario. 
11. No hay tablas.

El usuario sólo decide el movimiento, el programa debe encargarse de la evaluación y aplicación de las reglas (por tanto debe realizar automáticamente el proceso de "comidas múltiples", la promoción a reina, etc.)
