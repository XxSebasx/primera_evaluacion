def generar_cuadrado(longitud,valores):
   cuadrado = []
   lista_valores = valores.split(" ")
   contador = -1
   for fila in range(longitud):
       fila = []
       for columna in range(longitud):
           contador += 1
           fila.append(int(lista_valores[contador]))
       cuadrado.append(fila)
  
   return cuadrado

def calcular_constante_magica(cuadrado):
    return sum(cuadrado[0])

def comprobar_diabolico(cuadrado):
   longitud_cuadrado = len(cuadrado)
   constante_magica = calcular_constante_magica(cuadrado)

    #suma fila
   for fila in cuadrado:
       if(sum(fila) != constante_magica):
            return False
    
    #suma columna
   for fila in range(longitud_cuadrado):
        suma_columna = 0
        for columna in range(longitud_cuadrado):
            suma_columna +=  cuadrado[columna][fila]
        if(suma_columna != constante_magica):
            return False
  
   #suma diagonal primaria
   suma_diagonal_primaria = 0
   for fila in range(longitud_cuadrado):
       for columna in range(longitud_cuadrado):
           if(fila == columna):
               suma_diagonal_primaria += cuadrado[fila][columna]
    
   if(suma_diagonal_primaria != constante_magica):
       return False
  
   #suma diagonal secundaria
   suma_diagonal_secundaria = 0
   for fila in range(longitud_cuadrado):
       for columna in range(longitud_cuadrado):
           if(fila + columna == longitud_cuadrado -1):
               suma_diagonal_secundaria += cuadrado[fila][columna]
    
   if(suma_diagonal_secundaria != constante_magica):
        return False
    
   return True

def comprobar_esoterico_impar(cuadrado,n, constante_magica_2):
    esoterico = False
    esquinas = cuadrado[0][0] + cuadrado[0][n-1] + cuadrado[n-1][0] + cuadrado[n-1][n-1]
    mitad_longitud = int((n-1)/2)
    centro = 4 * cuadrado[mitad_longitud][mitad_longitud]
    centro_lados = cuadrado[mitad_longitud][0] + cuadrado[mitad_longitud][n-1] + cuadrado[0][mitad_longitud] + cuadrado[n-1][mitad_longitud]
    if(esquinas == constante_magica_2 and centro_lados == constante_magica_2 and centro == constante_magica_2):
        esoterico = True
    
    return esoterico


def comprobar_esoterico_par(cuadrado,n, constante_magica_2):
        esoterico = False
        esquinas = cuadrado[0][0] + cuadrado[0][n-1] + cuadrado[n-1][0] + cuadrado[n-1][n-1]
        mitad_longitud = int((n)/2)
        centro_lados = 0
        centro = 0
        for fila in range(n):
            for columna in range(n):
                if (fila == mitad_longitud and columna == 0 or fila == mitad_longitud - 1 and columna == 0 or fila == mitad_longitud and columna == n - 1
                    or fila == mitad_longitud - 1 and columna == n - 1 or columna == 0 and fila == mitad_longitud or 
                    columna == mitad_longitud - 1 and fila == 0 or columna == mitad_longitud and fila == n - 1
                    or columna == mitad_longitud - 1 and fila == n - 1 or columna == mitad_longitud and fila == 0):
                    centro_lados += cuadrado[fila][columna]
                
                if(fila == mitad_longitud and columna == mitad_longitud or fila == mitad_longitud and columna == mitad_longitud -1
                   or fila == mitad_longitud -1 and columna == mitad_longitud or fila == mitad_longitud-1 and columna == mitad_longitud -1):
                    centro += cuadrado[fila][columna]
        if(esquinas == constante_magica_2 and centro == constante_magica_2 and centro_lados == constante_magica_2 * 2):
            esoterico = True
        
        return esoterico

def comprobar_esoterico(cuadrado):
    esoterico = False
    n2 = len(cuadrado) ** 2
    for fila in range(len(cuadrado)):
            for columna in range(len(cuadrado)):
                if(cuadrado[fila][columna] > n2):
                    return esoterico
    constante_magica = calcular_constante_magica(cuadrado)
    n = len(cuadrado)
    constante_magica_2 = (4 * constante_magica)/n
    if(n%2 != 0):
        esoterico = comprobar_esoterico_impar(cuadrado,n,constante_magica_2)
    else:
        esoterico = comprobar_esoterico_par(cuadrado,n,constante_magica_2)

    
    return esoterico


def play():
    while True:
        longitud = int(input())
        if(longitud == 0):
            break
        numeros = input()
        cuadrado = generar_cuadrado(longitud,numeros)
        if(comprobar_diabolico(cuadrado)):
            if(comprobar_esoterico(cuadrado)):
                print("ESOTERICO")
            else:
                print("DIABOLICO")
        else:
            print("NO")


if __name__ == "__main__":
    play()
