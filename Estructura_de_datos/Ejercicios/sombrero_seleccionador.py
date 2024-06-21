REGISTRO_ESTUDIANTES = [{"nombre":"Harry Potter", "edad":11,"habilidades":["Vuelo en escoba", "Encantamientos"]},
                        {"nombre":"Sebas", "edad":11,"habilidades":["Astucia"]}]

casas = {
    "Gryffindor":[],
    "Slytherin":[],
    "Hufflepuff":[],
    "Ravenclaw":[]
}

CASAS_PREGUNTAS = {
    "Gryffindor":["Vuelo en escoba", "valentía", "habilidades de liderazgo", "dominio de duelos", "audacia", "extroversión", "transparencia"],
    "Slytherin":["Astucia", "habilidades en hechizos oscuros", "determinación", "manejo deserpientes", "ambición"],
    "Hufflepuff":["Lealtad", "amistad", "habilidades en herbología", "empatía", "paciencia","esfuerzo", "justicia y simpatía"],
    "Ravenclaw":["Inteligencia", "creatividad", "encantamientos", "adivinación", "sabiduría","habilidades en estudios mágicos"]}


def seleccionar_casa(estudiante):
    casas_puntos = {"Gryffindor":0,"Slytherin":0,"Hufflepuff":0,"Ravenclaw":0}
    for habilidad in estudiante["habilidades"]:
        for casa in CASAS_PREGUNTAS.keys():
            if(habilidad in CASAS_PREGUNTAS[casa]):
                casas_puntos[casa] += 1
    

    casa_seleccionada = ""
    puntos_casa_seleccionada = 0
    for casa_punto in casas_puntos.keys():
        if(casas_puntos[casa_punto] > puntos_casa_seleccionada):
            casa_seleccionada = casa_punto
    
    casas[casa_seleccionada] = estudiante


def simular_seleccion(estudiantes):
    for estudiante in estudiantes:
        seleccionar_casa(estudiante)
    
    for casa in casas:
        print(f'{casa}: {casas[casa]}')

if __name__ == "__main__":
    simular_seleccion(REGISTRO_ESTUDIANTES)
        

        