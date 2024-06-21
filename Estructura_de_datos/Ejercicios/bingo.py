import random
import time




DELAY = 0.8
LIMITE_INFERIOR = 100
LIMITE_SUPERIOR = 200
N_MINIMO_BOMBO = 1
N_MAXIMO_BOMBO = 90
TACHADO = 'X'




def crear_bombo():
   numeros_bombo = []
   for numero in range(N_MINIMO_BOMBO, N_MAXIMO_BOMBO + 1):
       numeros_bombo.append(numero)
 
   return numeros_bombo




def generar_numeros_serie(cantidad):
  numeros_series = []
  numeros_series_juego = []
  for numero in range(LIMITE_INFERIOR, LIMITE_SUPERIOR+1):
      numeros_series.append(numero)




  random.shuffle(numeros_series)


  for posicion in range(cantidad):
      numeros_series_juego.append(numeros_series[posicion])




  numeros_series_juego.sort()


  return numeros_series_juego








def generar_cartones(cantidad):
  numeros_bombo = crear_bombo()
  cartones = []
  numero_serie_juego = generar_numeros_serie(cantidad)




  poscion_n_serie = -1
  for n in range(cantidad):
      poscion_n_serie += 1
      numeros_carton = random.sample(numeros_bombo, 15)
      carton = {}
      traspuesta = []
      matriz = []
      contador = -1
      # matriz
      for fila in range(5):
          lista = []
          for columna in range(3):
              contador += 1
              lista.append(numeros_carton[contador])
          lista.sort()
          matriz.append(lista)
      # traspuesta
      for fila in range(3):
          lista = []
          for columna in range(5):
              lista.append(0)
          traspuesta.append(lista)


      # crear el carton
      for fila in range(3):
          for columna in range(5):
              traspuesta[fila][columna] = matriz[columna][fila]


      carton["serie"] = numero_serie_juego[poscion_n_serie]
      carton["numeros"] = traspuesta




      # añadir carton
      cartones.append(carton)
  return cartones






def imprimir_cartones(cartones):
  for carton in (cartones):
          print()
          print(f'carton nº{carton["serie"]: > 3}')
          print("----------------")




          for fila in carton["numeros"]:
              linea_formateada = ""
              for valor in fila:
                  if(valor == TACHADO):
                      valor = '\033[1;35m' + TACHADO + '\033[0;m'
                  linea_formateada += f'{valor: >2} '
              print(linea_formateada)
















def sacar_bola(bombo):
  random.shuffle(bombo)
  return bombo.pop(0)










def comprobar_linea(cartones,cartones_linea):
   carton_linea = {"serie":0,"fila":0}
   for carton in cartones:
       contador = 0
       linea = False
       tabla = carton["numeros"]
       for fila in tabla:
           contador += 1
           if(TACHADO  in fila):
               linea = True
               for valor in fila:
                   if(valor != TACHADO):
                       linea = False             
           if(linea):
                carton_linea["serie"] = carton["serie"]
                carton_linea["fila"] = contador
                if(carton_linea not in cartones_linea):   
                    return carton_linea
          
   return {}
      
      






  
 
 
 
         


def comprobar_bingo(cartones):
   tablero_tachado = []
   for fila in range(3):
      lista = []
      for columna in range(5):
          lista.append(TACHADO)
      tablero_tachado.append(lista)
 
   for carton in cartones:
       if(carton["numeros"] == tablero_tachado):
           return carton
    
   return {}
   






def tachar_tablero(cartones,bola):
   for carton in cartones:
       tabla = carton["numeros"]
       for fila in range(3):
           for columna in range(5):
               if(tabla[fila][columna] == bola):
                   tabla[fila][columna] = TACHADO


      




def play():
  n_jugadores = int(input("Dime la cantidad de jugadores: "))
  print("Comienta el juego con los siguientes cartones:")
  cartones = generar_cartones(n_jugadores)
  numeros_bombo = crear_bombo()
  cartones_linea = []
  bolas_sacadas = []
  imprimir_cartones(cartones)
  while True:
       bola = sacar_bola(numeros_bombo)
       bolas_sacadas.append(bola)
       bolas_sacadas_formato = str(bolas_sacadas).replace("[","").replace("]","").replace(",","")
       print("Numeros jugados hasta ahora: " + bolas_sacadas_formato)
       tachar_tablero(cartones,bola)
       imprimir_cartones(cartones)
       carton_linea = comprobar_linea(cartones,cartones_linea)
       if(carton_linea != {}):
           cartones_linea.append(carton_linea)
           print(f'LINEA! en la fila {carton_linea["fila"]} en el carton nº {carton_linea["serie"]}')
        
       ganador = comprobar_bingo(cartones)
       if(ganador != {}):
           print(f'BINGO!!! ha ganado el carton {ganador["serie"]}')
           break
     
       time.sleep(DELAY)

if __name__ == "__main__":
   play()
