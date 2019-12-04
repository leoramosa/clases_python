
personas = []
celular = []
resp = ""
def registrar():
    nom = input("Ingresar nombre:")
    cel = input("ingresar celular:")
    personas.append(nom)
    celular.append(cel)
def agenda_contacto():
    agenda_pri = input("ingresar numero de contacto:")
        if [""] in personas:
            print("exite contacto")
        else:
            print("persona no encontrada")
    #print(personas)
    #print(celular)
def menu():
    print("Menu Opciones")
    print("1.-Registrar Contacto")
    print("2.-Buscar contacto")
    opc = input("Escoja una opcion:")
    if opc == "1":
        registrar()
    elif opc == "2":
        agenda_contacto()
    else:
        exit()
while resp != "N":
    menu()
    resp = input("Desea Continuar:")