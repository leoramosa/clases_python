empleados = int(input("Ingrese el numero de empleado:"))
factura = int(input("Facturacion de soles:"))
balance = int(input("balance de la empresa:"))
if empleados < 50 and factura < 30000000 and balance <= 5000:
    print("Mype")
else:
    print("no mype")