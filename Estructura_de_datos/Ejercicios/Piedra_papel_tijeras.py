import random

def determinar_eleccion(opcion):
    eleccion = ""
    match opcion:
        case "t":
            eleccion = "tijeras"
        case "p":
            eleccion = "papel"
        case "x":
            eleccion = "piedra"
    
    return eleccion

def eleccion_ordenador():
    opcion_ordenador = ""
    numero_aleatorio= random.randint(1,3)
    match numero_aleatorio:
        case 1:
            opcion_ordenador = "t"
        case 2:
            opcion_ordenador = "p"
        case 3:
            opcion_ordenador = "x"
    
    return determinar_eleccion(opcion_ordenador)

def determinar_ganador(jugador, ordenador):
    resultado = "pierdes"
    jugador = determinar_eleccion(jugador)
    if(jugador == ordenador):
        return "empatas"
    
    match jugador:
        case "tijeras":
            if(ordenador == "papel"):
                resultado = "ganas"
        case "papel":
            if(ordenador == "piedra"):
                resultado = "ganas"
        case "piedra":
            if(ordenador == "tijeras"):
                resultado = "ganas"
    
    return resultado

def estadisticas(n_partidas, ganadas, perdidas, empatadas):
    porcentaje_ganadas = 0.0
    porcentaje_perdidas = 0.0
    porcentaje_empatadas = 0.0
    if( ganadas != 0):
        porcentaje_ganadas = 100 / (n_partidas/ganadas)
    if( perdidas != 0):
        porcentaje_perdidas = 100 / (n_partidas/perdidas)
    if( empatadas != 0):
        porcentaje_empatadas = 100 / (n_partidas/empatadas)
    

    print("Numero de partidas: " + str(n_partidas) )
    print("Yo gané: " + str(perdidas) + "(" + str(porcentaje_perdidas) + "%).")
    print("Tú ganaste: " + str(ganadas) + "(" + str(porcentaje_ganadas) + "%).")
    print("Hemos empatado: " + str(empatadas) + "(" + str(porcentaje_empatadas) + "%).")

def play():
    n_partidas = 0
    ganadas = 0
    perdidas = 0
    empatadas = 0
    while True:
        jugador = ""
        print("Tú turno")
        
        while True:
            jugador = input()
            if (jugador in "xstp"):
                break

            print("No existe ese gesto")
        
        if(jugador == "s"):
            break
        
        n_partidas += 1
        ordenador = eleccion_ordenador()
        print("Mi turno: " + ordenador)
        resultado_partida = determinar_ganador(jugador, ordenador)
        print(resultado_partida)
        match resultado_partida:
            case "empatas":
                empatadas += 1
            case "ganas":
                ganadas += 1
            case "pierdes":
                perdidas += 1
    
    estadisticas(n_partidas, ganadas, perdidas, empatadas)


if __name__ == "__main__":
    play()
        


                 
        


    
