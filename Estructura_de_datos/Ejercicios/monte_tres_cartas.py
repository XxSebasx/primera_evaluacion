import random
N = 20
PALOS = ["♠","♥","♣","♦"]
NUMEROS =["As", 1,2,3,4,5,6,7,8,9,10,"K","Q","J"]
def generar_mazo():
   mazo = []
   for palo in PALOS:
       for numero in NUMEROS:
           carta = (palo,numero)
           mazo.append(carta)
   return mazo


def sacar_cartas(mazo):
   cartas = []
   reina_corazones = mazo.pop(mazo.index(("♥","Q")))
   cartas.append(reina_corazones)
   for n_cartas in range(2):
       cartas.append(mazo.pop(mazo.index(random.choice(mazo))))
  
   random.shuffle(cartas)


   return cartas


def mover(cartas):
   movimiento = random.randint(1,6)
   match movimiento:
        case 1:
            print("izquierda a derecha")
            cartas[0], cartas[2] = cartas[2], cartas[0]
        case 2:
            print("derecha a izquierda")
            cartas[0], cartas[2] = cartas[2], cartas[0]
        case 3:
            print("centro a derecha")
            cartas[1], cartas[2] = cartas[2], cartas[1]
        case 4:
            print("derecha a centro")
            cartas[1], cartas[2] = cartas[2], cartas[1]
        case 5:
            print("centro a izquierda")
            cartas[0], cartas[1] = cartas[1], cartas[0]
        case 6:
            print("izquierda a centro")
            cartas[0], cartas[1] = cartas[1], cartas[0]
    


def comprobar_seleccion_carta(seleccion,cartas):
   return cartas[seleccion] == ("♥","Q")




def mostrar_carta(carta):
   print(" _____  _____  _____")
   print(f'|{carta[0][1]:<5}||{carta[1][1]:<5}||{carta[2][1]:<5}|')
   print(f'|{carta[0][0]:^5}||{carta[1][0]:^5}||{carta[2][0]:^5}|')
   print(f'|____{carta[0][1]:>1}||____{carta[1][1]:>1}||____{carta[2][1]:>1}|')
 
  






def play():
   mazo = generar_mazo()
   cartas = sacar_cartas(mazo)
   mostrar_carta(cartas)
   print()
   for n in range(N):
       mover(cartas)
  
   usuario = int(input("¿Donde esta la reina de corazones?: "))
   posicion = 0

   if(usuario == "centro"):
       posicion = 1
   else:
       posicion = 2


  
   print()
   if(comprobar_seleccion_carta(usuario,cartas)):
       print("Ganaste")
   else:
       print("Perdiste")
  
   mostrar_carta(cartas)
  


if __name__ == "__main__":
   print(sacar_cartas(generar_mazo()))
