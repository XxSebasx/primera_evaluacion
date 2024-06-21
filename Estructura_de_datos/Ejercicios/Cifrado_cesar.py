
from string import ascii_lowercase
def cifrar_texto(saltos,cadena):
    cadena = cadena.lower()
    cadena_cifrada = ""
    for letra in cadena:
        if(letra not in ascii_lowercase):
            cadena_cifrada += letra
        else:
            if(saltos > len(ascii_lowercase[ascii_lowercase.index(letra):]) - 1):
                cadena_cifrada += ascii_lowercase[saltos - len(ascii_lowercase[ascii_lowercase.index(letra):])]
            else:
                cadena_cifrada += ascii_lowercase[ascii_lowercase.index(letra) + saltos]
    
    return cadena_cifrada

def play():
    n_textos = int(input("¿Cuántos textos desea cifrar? "))
    for n in range(n_textos):
        texto = input("Introduce un texto para cifrar con cesar: ")
        n_saltos = int(input("Con qué salto quieres cifrar: "))
        print(cifrar_texto(n_saltos,texto))

if __name__ == "__main__":
    play()


                
