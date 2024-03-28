def trece_catorce():
    rango = int(input())
    for n in range (rango):
        cadena = input().split("-")
        izquierda = int(cadena[0])
        derecha = int(cadena[1])
        if(izquierda%2 == 0):
            if(izquierda+1 == derecha):
                print("SI")
            else:
                print("NO")
        elif(derecha%2 == 0):
            if(derecha+1 == izquierda):
                print("SI")
            else:
                print("NO")
        else:
            print("NO")

if __name__ == "__main__":
    trece_catorce()

    