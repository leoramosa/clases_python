estudiante1={
    "nombre":"armando",
    "tareas":[12,14,15,17,18],
    "pruebas":[20,18,16,16,17],
    "examenes":[17,15,18,15,19],
    "hobbies":["codea","running","parapente","musica"],
    "especialidad":"Back-end"
}

estudiante2 = {
    "nombre":"Carmen",
    "tareas":[17,12,15,17,18],
    "pruebas":[19,18,16,16,17],
    "examenes":[17,16,19,15,19],
    "hobbies":["codea","comen","bailar","pintar"],
    "especialidad":"Front-end"
}

estudiante3={
    "nombre":"Leonardo",
    "tareas":[12,17,17,17,17],
    "pruebas":[20,20,20,16,20],
    "examenes":[17,20,20,20,20],
    "hobbies":["codea","trotar","comer","nadar"],
    "especialidad":"Back-end"
}

#definir una variable para mostrar los elemnentos
indice = 0

#una lista donde almacenolos datos del estudiant
estudiantes = [estudiante1, estudiante2, estudiante3]

#hacemos el recorrido de nuestra lista para mostar cada elemento
#de forma individual

"""Est est in estudiantes:
    print(estudiantes[indice]["nombre"])
    print("tareas:",estudiantes[indice]["tareas"])
    print("Pruebas:", estudiantes[indice]["pruebas"])
    print("Examenes:", estudiantes[indice]["examenes"])
    print("Hobbies:", estudiantes[indice]["hobbies"])
    print("Especialidad:", estudiantes[indice]["especialidad"])
    indice += 1"""

for est in estudiantes:
    print(estudiantes[indice]["nombre"])
    print("Resumen de valores",est.values())
    print("Resumen de claves:",est.keys())
    indice += 1