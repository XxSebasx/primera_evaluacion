def sacar_digito_control(codigo):
    return int(codigo[-1])

def sacar_digito_comprobacion(codigo):
    codigo = codigo[:-1]
    codigo = codigo[::-1]
    suma_digitos = 0
    digito_comprobacion = 0
    for n in range(1,len(codigo)+1):
        if(n%2 != 0):
            suma_digitos += int(codigo[n -1]) * 3
        else:
            suma_digitos += int(codigo[n -1])*1
    
    while True:
        if(suma_digitos%10 == 0):
            break

        digito_comprobacion += 1
        suma_digitos += 1
    
    return digito_comprobacion

def comprobar_digitos(codigo):
    return sacar_digito_control(codigo) == sacar_digito_comprobacion(codigo)

def determinar_pais(codigo):
    pais = "desconocido"
   
    if(codigo[0:2] == "50"):
            pais = "Inglaterra"
    elif(codigo[0:3] == "539"):
            pais = "Irlanda"
    elif(codigo[0:3] == "560"):
            pais = "Portugal"
    elif(codigo[0:3] == "850"):
            pais = "Cuba"
    elif(codigo[0:3] == "890"):
            pais = "India"
    elif(codigo[0:2] == "70"):
            pais = "Noruega"
    elif(codigo[0:3] == "759" ):
            pais = "Venezuela"
    elif(codigo[0] == "0"):
            pais = "EEUU"
    elif(codigo[0:3 == "380"]):
            pais = "Bulgaria"
    
    return pais
    



def play():
    while True:
        codigo = input()
        if(codigo == "0"):
            break
        
        if(comprobar_digitos(codigo)):
            if(len(codigo) == 8):
                print("SI")
            else:
                print("SI " + str(determinar_pais(codigo)))
        else:
            print("NO")
            
            


if __name__ == "__main__":
   play()
  
    

