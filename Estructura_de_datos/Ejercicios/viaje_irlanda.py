COLUMNAS = "ABCDEF"
MIN_FILAS = 5
MAX_FILAS = 35
def generar_asientos():
   asientos = {}
   for fila in range(MIN_FILAS,MAX_FILAS):
        diccionario_columnas = {}
        for columna in COLUMNAS:
            diccionario_columnas[columna] = "----------"
        asientos[fila] = diccionario_columnas
    
   return asientos

def mostrar_asientos(asientos):
    print(f'{COLUMNAS[0]:>13}{COLUMNAS[1]:>12}{COLUMNAS[2]:>12}{COLUMNAS[3]:>11}{COLUMNAS[4]:>10}{COLUMNAS[5]:>11}')
    for fila in range(MIN_FILAS,MAX_FILAS):

        print(f'row {fila: 03}: {asientos[fila][COLUMNAS[0]]:>10} {asientos[fila][COLUMNAS[1]]:>10} {asientos[fila][COLUMNAS[2]]:>10}|'
       f'{asientos[fila][COLUMNAS[3]]:>10} {asientos[fila][COLUMNAS[4]]:>10} {asientos[fila][COLUMNAS[5]]:>10}')

def seleccionar_asiento(asientos,asiento,alumno):
    columna = asiento[-1]
    fila = int(asiento[:-1])
    asientos[fila][columna] = alumno

def play():
    sevilla_dublin = generar_asientos()
    dublin_sevilla = generar_asientos()
    n_alumnos = int(input())
    for n in range(n_alumnos):
        alumno = input().split(" ")
        nombre_alumno = alumno[0]
        asiento_sevilla = alumno[1]
        asiento_dublin = alumno[2]

        seleccionar_asiento(sevilla_dublin,asiento_sevilla,nombre_alumno)
        seleccionar_asiento(dublin_sevilla,asiento_dublin,nombre_alumno)
    
    print("SEVILLE-DUBLIN")
    print()
    mostrar_asientos(sevilla_dublin)
    print()
    print("DUBLIN-SEVILLE")
    print()
    mostrar_asientos(dublin_sevilla)
        




if __name__ == "__main__":
   play()
    

      
      
      

