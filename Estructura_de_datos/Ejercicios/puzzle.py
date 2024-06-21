import random
N = 4
def generar_tablero_objetivo():
    matriz = []
    contador = 0
    for fila in range(N):
        lista = []
        for columna in range(N):
            contador += 1
            if(contador == N*N):
                lista.append(0)
            else:
                lista.append(contador)
        matriz.append(lista)
    
    return matriz

def generar_tablero_juego():
    contador = -1
    matriz = []
    lista_numeros = []
    for numero in range(N*N):
        lista_numeros.append(numero)
    
    random.shuffle(lista_numeros)

    for fila in range(N):
        lista = []
        for columna in range(N):
            contador += 1
            lista.append(lista_numeros[contador])
        matriz.append(lista)
    
    return matriz

def imprimir_tablero(tablero):
    for fila in tablero:
        fila_formateada = ""
        for valor in fila:
            if(valor == 0):
                valor = ""
            fila_formateada += f'{valor: >2}|'
        print(fila_formateada)

def determinar_movimientos(tablero):
    movimientos_disponibles = "WASD"
    fila_vacio = 0
    columna_vacio = 0
    for fila in range(len(tablero)):
        for columna in range(len(tablero)):
            if(tablero[fila][columna] == 0):
                fila_vacio = fila
                columna_vacio = columna
                break
    
    if(fila_vacio == 0 and columna_vacio == 0):
        movimientos_disponibles = "AW"
    elif(fila_vacio == 0 and columna_vacio == N-1):
        movimientos_disponibles = "DW"
    elif(columna_vacio == 0 and fila_vacio == N-1):
        movimientos_disponibles = "AS"
    elif(columna_vacio == N-1 and fila_vacio == N-1):
        movimientos_disponibles = "DS"
    elif(columna_vacio > 0 and columna_vacio < N-1 and fila_vacio == 0):
        movimientos_disponibles = "ADW"
    elif(columna_vacio > 0 and columna_vacio < N-1 and fila_vacio == N-1):
        movimientos_disponibles = "ADS"
    elif(fila_vacio > 0 and fila_vacio < N-1 and columna_vacio == 0):
        movimientos_disponibles = "AWS"
    elif(fila_vacio > 0 and fila_vacio < N-1 and columna_vacio == N-1):
        movimientos_disponibles = "DWS"

    
    return movimientos_disponibles

def mover_pieza(tablero,movimiento):
    fila_vacio = 0
    columna_vacio = 0
    for fila in range(len(tablero)):
        for columna in range(len(tablero)):
            if(tablero[fila][columna] == 0):
                fila_vacio = fila
                columna_vacio = columna
                break
    
    match movimiento:
        case "W":
            aux = tablero[fila_vacio][columna_vacio]
            tablero[fila_vacio][columna_vacio] = tablero[fila_vacio + 1][columna_vacio]
            tablero[fila_vacio + 1][columna_vacio] = aux
        case "S":
            aux = tablero[fila_vacio][columna_vacio]
            tablero[fila_vacio][columna_vacio] = tablero[fila_vacio - 1 ][columna_vacio]
            tablero[fila_vacio - 1][columna_vacio] = aux
        case "A":
            aux = tablero[fila_vacio][columna_vacio]
            tablero[fila_vacio][columna_vacio] = tablero[fila_vacio][columna_vacio + 1]
            tablero[fila_vacio][columna_vacio + 1] = aux
        case "D":
            aux = tablero[fila_vacio][columna_vacio]
            tablero[fila_vacio][columna_vacio] = tablero[fila_vacio][columna_vacio - 1]
            tablero[fila_vacio][columna_vacio - 1] = aux

def play():
    tablero_objetivo = generar_tablero_objetivo()
    tablero_juego = generar_tablero_juego()
    while True:
        imprimir_tablero(tablero_juego)
        if(tablero_juego == tablero_objetivo):
            break
        posibles_movimientos = determinar_movimientos(tablero_juego)
        print()
        print("Movimientos posibles: " + posibles_movimientos)
        jugador = ""
        while True:
            jugador = input()
            if(jugador in posibles_movimientos):
                break
            print("No puedes mover en esa direccion")
        
        mover_pieza(tablero_juego,jugador)
    
    print("Ganaste!")







if __name__ == "__main__":
    play()

   

