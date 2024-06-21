import random
palabras_secretas = ["reingenieria", "cubeta", "tunelizacion", "protocolo", "puertos", "conexion", "broadcasting",
                     "direccion", "internet", "router", "switch", "wifi", "estandar", "socket", "transporte", "enlace",
                     "capas", "arquitectura", "cliente", "servidor", "proxy", "firewall", "redes", "LAN", "WAN", "MAN",
                     "hub", "concentrador", "datagrama", "puente", "fibra", "TCP", "UDP", "mascara", "gateway",
                     "servidor", "DNS", "cliente", "conmutacion", "circuito", "satelite", "coaxial", "microondas",
                     "infrarrojos", "token", "anillo", "bus", "control", "flujo", "congestion", "enrutamiento",
                     "aplicacion", "correo", "peertopeer"]

AHORCADO = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']


def sacar_palabra():
    return random.choice(palabras_secretas)

def sacar_palabra_oculta(palabra_secreta):
    return list("-"*len(palabra_secreta))

def comprobar_palabra(palabra, palabra_secreta):
    ganador = False
    if(palabra == palabra_secreta):
        ganador = True
    return ganador

def comprobar_letra(palabra_secreta,letra,palabra_mostrar):
    contiene_letra = False
    if(letra in palabra_secreta):
        contiene_letra = True
        for posicion_letra in range(len(palabra_secreta)):
            if(letra == palabra_secreta[posicion_letra]):
                palabra_mostrar[posicion_letra] = letra
    return contiene_letra

def play():
    palabra_secreta = sacar_palabra()
    palabra_oculta = sacar_palabra_oculta(palabra_secreta)
    cadena_oculta = ''.join(palabra_oculta)
    ganador = False
    perdidas = -1
    intentos = 0
    print(cadena_oculta)
    while not ganador and perdidas < 6:
        jugador = input("Ingresa una letra o la palabra a adivinar:")
        intentos += 1
        if(len(jugador) > 1):
            ganador = comprobar_palabra(jugador, palabra_secreta)
            if(not ganador):
                print("No es esa la palabra secreta. Llevas" + intentos + " intentos: " + str(cadena_oculta))
        else:
            contiene_letra = comprobar_letra(palabra_secreta,jugador,palabra_oculta)
            if(contiene_letra):
                cadena_oculta = ''.join(palabra_oculta)
                print(f'Intento {intentos}: {cadena_oculta}')
                if(cadena_oculta == palabra_secreta):
                    ganador = True
            else:
                perdidas += 1
                print(AHORCADO[perdidas])
    
    if(ganador):
        print("Enhorabuena!! Adivinaste en " + str(intentos) + " intentos")
    else:
        print(AHORCADO[perdidas])
        print("Perdiste")




if __name__ == "__main__":
   play()