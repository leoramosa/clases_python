# c = 0
# for i in ranger(1, 20):
#   if 1 % 2 == =:
#   c = c + 1
#   print(c)


"""sum = 0
con = 0
for i in range(0, 5):
    nota = int(input("Ingresar Notas del alumno:"))
    #sum = sum + nota
    sum += nota
#prom = sum // 5
    #con =  con + 1 #contador
    con += 1
prom = sum / con
#print(sum)
print("El promedio del alumno es  {}".format(prom))"""
# and todas las condiciones deben ser verdad
# or basta que una condicion debe ser verdad
sum = 0
con = 0
for i in range(0, 5):
    nota = int(input("ingresar notas del alumno:"))
    if nota >= 1 and nota <= 20:
        sum += nota
        con += 1
    else:
        print("Nota invalida")
        #nota = int(input("Ingrese notas del alumno:"))
prom = sum / con
print("El promedio del alumno es {}".format(prom))