def conversor():
    cadena_nueva = ""
    linea = input().split(" ")
    palabra = linea[0]
    opcion = linea[1]
    match opcion:
        case "snake_case":
            for letra in palabra:
                if(letra == "-"):
                    cadena_nueva+= "_"
                elif(letra.isupper()):
                    if(letra == palabra[0]):
                        cadena_nueva += letra.lower()
                    else:
                        cadena_nueva += "_"+letra.lower()
                else:
                    cadena_nueva += letra
        case "kebab-case":
            for letra in palabra:
                if(letra == "_"):
                    cadena_nueva+= "-"
                elif(letra.isupper()):
                    if(letra == palabra[0]):
                        cadena_nueva += letra.lower()
                    else:
                        cadena_nueva += "-"+letra.lower()
                else:
                    cadena_nueva += letra 
        case "CamelCase":
            separacion = palabra.title()
            for letra in separacion:
                if(letra != "-" and letra != "_"):
                    cadena_nueva += letra
    
    return cadena_nueva




if __name__ == "__main__":
    print(conversor())