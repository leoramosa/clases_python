


"""def sumar(valor1, valor2):
    res = valor1 + valor2
    return res

def restar(valor1, valor2):
    res = valor1 - valor2
    #return res
    print(res)

restar(344, 34)"""

#print(sumar(58, 34))
#print(restar(88, 55))


# Una Funcion es un bloque de codigo dentro de mi programa
# que generalmente recibe parametros , tiene un proceso
# por hacer y generalmente nos retorna un valor
alumnos = []
resp = ""
def registrar():
    nom = input("Ingresar el Nombre:")
    alumnos.append(nom)
def listar():
    print(alumnos)
def menu():
    print("Menu de Opciones")
    print("1.-Registrar Alumnos")
    print("2.-Listar Alumnos")
    print("3.-Salir del Menu")
    opc = input("Ingrese Opcion:")
    if opc == "1":
        registrar()
    elif opc == "2":
        listar()
    else:
        exit()
while resp != "N":
    menu()
    resp = input("Desea Continuar:")