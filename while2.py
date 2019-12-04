passw = "codigo"
cont = 0
while True:
    con = input("Contraseña:")
    if con == passw:
        print("bienvenido al sistema")
        break #false va a salir del while - bucle
    else:
        print("contraseña errara")
        cont += 1
        if cont == 3:
            print("Cuenta bloqueda")
            break