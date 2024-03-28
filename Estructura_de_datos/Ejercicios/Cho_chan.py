import random
D1 = ['+-------+',
      '|       |',
      '|   O   |',
      '|       |',
      '+-------+']

D2 = ['+-------+',
      '| O     |',
      '|       |',
      '|     O |',
      '+-------+']

D3 = ['+-------+',
      '| O     |',
      '|   O   |',
      '|     O |',
      '+-------+']

D4 = ['+-------+',
      '| O   O |',
      '|       |',
      '| O   O |',
      '+-------+']

D5 = ['+-------+',
      '| O   O |',
      '|   O   |',
      '| O   O |',
      '+-------+']

D6 = ['+-------+',
      '| O   O |',
      '| O   O |',
      '| O   O |',
      '+-------+']

def sacar_dado(numero):
    dado = []
    match numero:
        case 1:
            dado = D1
        case 2:
            dado = D2
        case 3:
            dado = D3
        case 4:
            dado = D4
        case 5:
            dado = D5
        case 6:
            dado = D6
    
    return dado

def sacar_numero_japones(numero):
    numero_japones = ""
    match numero:
        case 1:
            numero_japones = "ICHI"
        case 2:
            numero_japones = "NI"
        case 3:
            numero_japones = "SAN"
        case 4:
            numero_japones = "SHI"
        case 5:
            numero_japones = "GO"
        case 6:
            numero_japones = "ROKU"
    
    return numero_japones
    
            
            

def impresion_dados(numero1, numero2):
    dado1 = sacar_dado(numero1)
    dado2 = sacar_dado(numero2)
    for n in range(0,len(D1)):
        print(dado1[n] + "  " + dado2[n])

def play():
    dinero = 5000
    while dinero > 0:
        print("Tienes " + str(dinero) + " euros. " + "¿Cuanto apuestas (o SALIR)?")
        jugador = input()
        if(jugador == "SALIR" or dinero == 0):
            break

        dinero_apostado = int(jugador)
        print("El crupier...")
        print("CHO (par) or HAN (impar)?")
        eleccion_jugador = input()
        dado_1 = random.randint(1,6)
        dado_2 = random.randint(1,6)
        print("El crupier revela los dados:")
        print(sacar_numero_japones(dado_1) + " - " + sacar_numero_japones(dado_2))
        impresion_dados(dado_1, dado_2)
        suma = dado_2 + dado_1
        if(suma%2 == 0):
            if(eleccion_jugador == "CHO"):
                print("HAS GANADO")
                print("La casa se lleva un " + str(int(dinero_apostado * 0.10)))
                dinero += dinero_apostado
            else:
                print("HAS PERDIDO")
                dinero -= dinero_apostado
        else:
            if(eleccion_jugador == "HAN"):
                print("HAS GANADO")
                print("La casa se lleva un " + str(int(dinero_apostado * 0.10)))
                dinero += dinero_apostado
            else:
                print("HAS PERDIDO")
                dinero -= dinero_apostado
        










if __name__ == "__main__":
    play()