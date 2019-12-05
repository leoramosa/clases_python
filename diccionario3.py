mi_diccionario ={"bolivia":"la paz","chile":"santiago","uruguay":"montevideo"}
#imprime diccionario
print(mi_diccionario)
#imprimir un valor especifico
print(mi_diccionario["bolivia"])
#agregar un valor al diccionario
mi_diccionario["peru"]="lima"
#modificar un valor
mi_diccionario["peru"]="arequipa"
print(mi_diccionario)
#eliminar un valor
del mi_diccionario["peru"]
print(mi_diccionario)
#mostrar los valores del diccionario
print(mi_diccionario.values())
print(mi_diccionario.keys())  