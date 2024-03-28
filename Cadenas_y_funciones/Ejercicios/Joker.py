def joker():
    rango = int(input())
    for n in range (rango):
        solucion = "PIERDES"
        lista = input().split(" ")
        sorteo = sorted(lista[0])
        boleto = sorted(lista[1])
        if(sorteo == boleto):
            solucion = "GANAS"
        print(solucion)
        
        
                    
            

if __name__ == "__main__":
    joker()