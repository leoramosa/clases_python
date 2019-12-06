tienda_santa = {
        "venta_enero": "1444",
        "venta_febrero": "454554", 
        "venta_mayo": "144554",
        "venta_junio": "14432",
        "venta_julio": "1444",
        "venta_agosto": "19884",
        "venta_setiembre": "1884",
        "venta_octubre": "9933",
        "venta_noviembre": "943444",
        "venta_diembre": "3444"
}

tienda_chorrillos = {
        "venta_enero": "1444",
        "venta_febrero": "76554",
        "venta_marzo": "1458844",
        "venta_abril": "7774",
        "venta_mayo": "144554",
        "venta_junio": "14432",
        "venta_julio": "1444",
        "venta_agosto": "19884",
        "venta_setiembre": "1884",
        "venta_octubre": "9933",
        "venta_noviembre": "943444",
        "venta_diembre": "3444"
}

tienda_ate = {
        "venta_enero": "1444",
        "venta_febrero": "18854",
        "venta_marzo": "1458844",
        "venta_abril": "7774",
        "venta_mayo": "144554",
        "venta_junio": "14432",
        "venta_julio": "1444",
        "venta_agosto": "19884",
        "venta_setiembre": "1884",
        "venta_octubre": "9933",
        "venta_noviembre": "943444",
        "venta_diembre": "3444"
}

tienda_lince = {
        "venta_enero": "1444",
        "venta_febrero": "18854",
        "venta_marzo": "1458844",
        "venta_abril": "7774",
        "venta_mayo": "144554",
        "venta_junio": "14432",
        "venta_julio": "1444",
        "venta_agosto": "19884",
        "venta_setiembre": "1884",
        "venta_octubre": "9933",
        "venta_noviembre": "943444",
        "venta_diembre": "3444"
}
tiendas = [tienda_santa, tienda_chorrillos, tienda_ate, tienda_lince]
resp = ""

def media_tienda():
    print()
def febrero_():
    indice = 0
    mayor_febrero = 0
    while indice<len(tiendas["venta_febrero"]):
        if tiendas["venta_febrero"][indice]>mayor_febrero:
            mayor_febrero = tiendas["venta_febrero"][indice]
            indice += 1
    print(mayor_febrero)
    #for tie in tiendas:
        #print(tiendas[indice]["venta_febrero"])
        #indice += 1
def menu():
    print("Menu Opciones")
    print("1.-Media de ventas de todas tiendas:")
    print("2.-Tienda que genero mas en el mes de febrero")
    print("3.-tienda que genero mas en el mes de diciembre y julio:")
    opc = input("Seleccionar una opcion:")
    if opc == "1":
        media_tienda()
    elif opc == "2":
        febrero_()
    else:
        exit()
while resp != "N":
    menu()
    resp = input("Desea Continuar:")

