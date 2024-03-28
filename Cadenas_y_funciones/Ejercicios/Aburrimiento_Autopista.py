
def calcula_matricula():
    rango = int(input())
    for n in range (rango):
        antiguos = 0
        nuevos = 0
        matriculas = input().split(" ")
        matricula_Edu = matriculas[0]
        for i in range(1,len(matriculas)-1):
            matricula = matriculas[i]
            if(matricula[4:] != matricula_Edu[4:]):
                if(matricula_Edu[4:] > matricula[4:]):
                    antiguos+=1
                else:
                    nuevos += 1
            else:
                if(matricula_Edu[0:4] > matricula[0:4]):
                    antiguos+=1
                else:
                    nuevos += 1
        
        print(str(antiguos) + " " + str(nuevos))


            


if __name__ == "__main__":
   calcula_matricula()