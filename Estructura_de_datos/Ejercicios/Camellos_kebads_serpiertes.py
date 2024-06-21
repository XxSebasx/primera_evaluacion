from string import ascii_letters
def convertir_snake_case(cadena):
    cadena_convertida = ""
    if("-" in cadena):
        cadena_convertida = cadena.replace("-","_")
    else:
        for letra in cadena:
            if(letra.islower()):
                cadena_convertida += letra
            else:
               letra = letra.lower()
               if(letra == cadena[0].lower()):
                   cadena_convertida += letra
               else:
                   cadena_convertida += "_" + letra
    return cadena_convertida

def convertir_CamelCase(cadena):
    cadena_convertida = ""
    cadena = cadena.title()
    for letra in cadena:
        if(letra in ascii_letters):
            cadena_convertida += letra
    
    return cadena_convertida

def convertir_kebad_case(cadena):
    cadena_convertida = ""
    if("_" in cadena):
        cadena_convertida = cadena.replace("_","-")
    else:
        for letra in cadena:
            if(letra.islower()):
                cadena_convertida += letra
            else:
               letra = letra.lower()
               if(letra == cadena[0].lower()):
                   cadena_convertida += letra
               else:
                   cadena_convertida += "-" + letra
    return cadena_convertida

def play():
    while True:
        usuario = input().split(" ")
        cadena = usuario[0]
        opcion = usuario[1]
        match opcion:
            case "snake_case":
                print(convertir_snake_case(cadena))
            case "kebab-case":
                print(convertir_kebad_case(cadena))
            case "CamelCase":
                print(convertir_CamelCase(cadena))



if __name__ == "__main__":
    play()

    
    

        

    