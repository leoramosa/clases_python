"""1.-Un Restaurante ofrece un descuento del 10% para consumos
de hasta s/.100 soles , un descuento de 20%  para consumos
mayores  y para ambos casos aplica un impuesto del 15% ,
determinar el importe a pagar por lo consumido
mostrando todos los importes"""

"""consumo = float(input("ingrese el monto consumido:"))
if consumo <= 100:
    des = consumo * 0.10
else:
    des = consumo * 0.20
imp = consumo *0.15
total = (consumo - des) + imp
print("El descuento: {}, el impuesto {}, el total {}".format(des, imp, total))"""

horas = float(input("ingres las horas trabajadas: "))
if horas > 40:
    sal_b = 4000/4
else:
    sal_b = 4000
salario = 4000
imp = salario *0.10
sal_n = (salario - imp)

print("Sal_b: {}, el sal_n: {}, imp: {}".format(sal_b, sal_n, imp))




