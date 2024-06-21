N = 10
barcos_jugador1 = [(1, 4), (1, 5), (1, 6), (1, 7), (3, 2), (4, 2), (5, 2), (7, 1), (7, 2), (7, 3), (7, 4)]
barcos_jugador2 = [(0, 1), (0, 2), (0, 3), (0, 4), (2, 5), (2, 6), (4, 7), (4, 8), (6, 9)]

def generar_tableros():
    tablero1 = []
    tablero2 = []
    for fila in range(N):
        lista1 = []
        lista2 = []
        for columna in range(N):
            lista1.append("~")
            lista2.append("~")
        tablero1.append(lista1)
        tablero2.append(lista2)
    return {"jugador_1" : tablero1, "jugador_2":tablero2}


def colocar_barcos(tableros):
    for tablero in tableros.keys():
        for fila in range(N):
            for columna in range(N):
                tupla = (fila,columna)
                if(tablero =="jugador_1" and tupla in barcos_jugador1):
                    tableros[tablero][fila][columna] = "B"
                elif(tablero =="jugador_2" and tupla in barcos_jugador2):
                    tableros[tablero][fila][columna] = "B"


def hundir_barco(jugador,tableros,tablero_enemigo):
    tableros[tablero_enemigo][jugador[0]][jugador[1]] = "O"
    if(tablero_enemigo == "jugador_1"):
        if(jugador in barcos_jugador1):
            tableros[tablero_enemigo][jugador[0]][jugador[1]] = "X"
            barcos_jugador1.remove(jugador)
    else:
        if(jugador in barcos_jugador2):
            tableros[tablero_enemigo][jugador[0]][jugador[1]] = "X"
            barcos_jugador2.remove(jugador)


def comprobar_ganador():
    return barcos_jugador1 == [] or barcos_jugador2 == []


def mostrar_tableros(tableros):
    for fila in range(N):
        fila_formateada_1 = ""
        fila_formateada_2 = ""
        for columna in range(N):
            fila_formateada_1 += f'{tableros["jugador_1"][fila][columna]:>2}'
            fila_formateada_2 += f'{tableros["jugador_2"][fila][columna]:>2}'
        print(f'{fila_formateada_1}||{fila_formateada_2}')



def play():
    contador = 0
    tablero_enemigo = "jugador_2"
    tableros = generar_tableros()
    colocar_barcos(tableros)
    while True:
        mostrar_tableros(tableros)
        if(comprobar_ganador()):
            break
        jugador = input("Te toca jugador: ").split(",")
        tupla = (int(jugador[0]),int(jugador[1]))
        hundir_barco(tupla,tableros,tablero_enemigo)
        contador+= 1
        if(contador %2 != 0):
            tablero_enemigo = "jugador_1"
        else:
            tablero_enemigo = "jugador_2"



if __name__ == "__main__":
    play()

    
    
        



