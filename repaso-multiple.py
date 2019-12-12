# Datos de entrada
nh = int(input("Ingrese el numero de hijos:"))
nhe = int(input("Numero de Hijos en edad escolar:"))
ec = input("Estado Civil de la Madre:")
subsidio = 0
# Para hallar el Monto 1
if nh <= 2:
    subsidio = 72
elif nh >= 3 and nh <= 5:
    subsidio = 90
else:
    subsidio = 120
# Para Hallar el Monto2
subsidio += 10 * nhe
if ec == 'v':
    subsidio += 20
else:
    subsidio += 0
print("El monto a Percibr es {}".format(subsidio))