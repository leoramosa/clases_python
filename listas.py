
#indice    0         1        2     3
alumnos = ["henry","jose","pedro","manuel"]



notas = [20,16,17,50]
valores = ["juan",True,20.78,50]
#diccionarios
clientes = {"a100:juan","a200:pedro"}
provee = {"prove:[100,200,500]"}

#tuplas
cursos = ("python","flask","django")

# print(type(alumnos))
# print(type(clientes))
# print(type(cursos)) 
print(alumnos)
print(alumnos[2]) #pedro
alumnos[2]="mario" #modificar el valor
alumnos.append("leonardo") #agregar un valor al final de la lista
alumnos.insert(1,"felipa") #agregar un valor donde se menciona 
alumnos.pop(1)
#ordenar la lista, ordena ascendente a-z
alumnos.sort()
#ordenar lista, ordena descendente z-a
alumnos.reverse()
print(alumnos)

alumnos.append("henry")
print(alumnos)
#count cuenta las veces que se repite un valor en la lista
alumnos.count("henry")
print(alumnos.count("henry"))

#contar todos los elementos que tiene la lista
contar =len(alumnos)
print(contar)

#elimina el elemento de la lista por su valor (el primer elemento lo elimina)
alumnos.remove("henry")
print(alumnos)




#eliminar valores de la lista

# alumnos.pop()