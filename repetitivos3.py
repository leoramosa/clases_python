#contadores
#acumuladores
c = 0
sum = 0
for i in range(12):
   valor = int(input("valores mensuales:"))
   c += 1 #contar las veces que el bucle da la vuelta
   sum += valor #sumar los valores que el bucle da la vuelta
print("cantidad de valores", c)
print("suma de valores", sum)