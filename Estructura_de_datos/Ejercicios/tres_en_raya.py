import random
FICHA_JUGADOR = "X"
FICHA_MAQUINA = "O"
def generar_tablero():
    tablero = {}
    for clave in range(1,9+1):
        tablero[clave] = " "
    return tablero

def mostrar_tablero(tablero):
    print(f'{tablero[1] :>2}|{tablero[2] :>3}|{tablero[3] :>2}')
    print("--+---+--")
    print(f'{tablero[4] :>2}|{tablero[5] :>3}|{tablero[6] :>2}')
    print("--+---+--")
    print(f'{tablero[7] :>2}|{tablero[8] :>3}|{tablero[9] :>2}')

def colocar_ficha(tablero, posicion,ficha):
    tablero[posicion] = ficha

def colocar_ficha_maquina(tablero):
    posicion = 0
    while True:
        posicion = random.randint(1,9)
        if(tablero[posicion] == " "):
            break
    
    colocar_ficha(tablero,posicion,FICHA_MAQUINA)

def comprobar_ganador(tablero):
    ganador = -1
    if (tablero[1] == tablero[2] == tablero[3] != " " or
        tablero[4] == tablero[5] == tablero[6] != " " or
        tablero[7] == tablero[8] == tablero[9] != " " or
        tablero[1] == tablero[4] == tablero[7] != " " or
        tablero[2] == tablero[5] == tablero[8] != " " or
        tablero[3] == tablero[6] == tablero[9] != " " or
        tablero[1] == tablero[5] == tablero[9] != " " or
        tablero[3] == tablero[5] == tablero[7] != " "):
        ganador = 1
    elif " " not in list(tablero.values()):
        ganador = 0

    return ganador

def play():
    tablero = generar_tablero()
    ganador = 0
    contador = 0
    mostrar_tablero(tablero)
    while True:
        jugador = 0
        while True:
            jugador = int(input("Tu turno: "))
            if(jugador > 9 or jugador < 1):
                print("Posicion inexistente")
            elif(tablero[jugador] == " "):
                break
            else:
                print("Posicion ocupada")
        
        colocar_ficha(tablero,jugador,FICHA_JUGADOR)
        mostrar_tablero(tablero)
        contador += 1
        ganador = comprobar_ganador(tablero)
        if(ganador == 1 or ganador == 0):
            break
        print("Mi turno:")
        colocar_ficha_maquina(tablero)
        mostrar_tablero(tablero)
        contador += 1
        ganador = comprobar_ganador(tablero)
        if(ganador == 1 or ganador == 0):
            break
        
    if(ganador == 1):
        if(contador%2 == 0):
            print("GANA EL JUGADOR " + FICHA_MAQUINA)
        else:
            print("GANA EL JUGADOR " + FICHA_JUGADOR)
    else:
        print("TABLAS")




if __name__ == "__main__":
    play()
