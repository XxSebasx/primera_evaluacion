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


def mostrar_dados(numero, otro_numero):
    dado = dado_mostrar(numero)
    otro_dado  = dado_mostrar(otro_numero)
    for fila in range(len(dado)):
        print(f'{dado[fila]}   {otro_dado[fila]}')

def sacar_dado():
    return random.randint(1,6)

def nombre_dado(numero):
    nombre = "ICHI"
    match numero:
        case 2:
            nombre = "NI"
        case 3:
            nombre = "SAN"
        case 4:
            nombre = "SHI"
        case 5:
            nombre = "GO"
        case 6:
            nombre = "ROKU"
    
    return nombre

def dado_mostrar(numero):
    dado = D1
    match numero:
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

def play():
    print("""Este juego de dados tradicional japonés, el croupier, sentado en el suelo, 
    lanza los dados en un cubilete de babumbu. El jugador debe adivinar si los dados 
    suman un número par(cho) o impar(han)""")
    dinero = 5000
    while dinero != 0:
        dinero_apostado = input(f'Tienes {dinero} euros. ¿Cuánto apuestas?')
        if(dinero_apostado == "SALIR"):
            break
        
        dinero_apostado = int(dinero_apostado)
        print("""El crupier hace girar el cubilete y se oye el traqueteo de los dados.
        El crupier golpea el cubilete contra el suelo, todavia cubriendo los dados y pide tu apuesta""")

        jugador = input("CHO(par) or HAN(impar)?")
        print("El crupier levanta el cubilete para revelar: ")
        n_dado_1 = sacar_dado()
        n_dado_2 = sacar_dado()
        print(f'{nombre_dado(n_dado_1)}  -  {nombre_dado(n_dado_2)}')
        print()
        mostrar_dados(n_dado_1, n_dado_2)
        
        ganas = False
        suma = n_dado_1 + n_dado_2
        if(jugador == "CHO" and suma%2 == 0 or jugador == "HAN" and suma%2 != 0):
            ganas = True
        
        if(ganas):
            dinero += dinero_apostado
            print(f'¡Has ganado! Tienes {dinero} euros')
            print(f'La casa se lleva {dinero_apostado *(10/100)} euros en tasas')
        else:
            dinero -= dinero_apostado
            print("¡Has perdido!")



if __name__ == "__main__":
    play()