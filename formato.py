#ejemplo1 de formato

First_Name = 'john'
Last_Name = 'Smith'
Full_Name = First_Name + " " + Last_Name
print("hi, name is {}".format(Full_Name))


#ejemplo1 de formato

mentor ="Sebastian"
curso = "Front"  
edad = 39
Salario = 200.8998777
print(mentor,"Dicta el curso",curso)
print("{} Dicta el curso {}".format(mentor,curso))


#conversion

sueldo = "2000"
Bon = 20
total = int(sueldo) + Bon
print(total)
 

#conversion de datos - Cast

# Hours = int(input("Enter Hours:")) # 5 horas
# Rate = float(input("Enter Rate:")) #cobro por hora
# salary = Hours * Rate
# print("pay: {0:.2f}".format(salary))

print("Hola, %s!" %mentor)
print("hola {}".format(mentor))

print("%s tiene %d años" %(mentor,edad))
print("%s tiene como salario %.2f" %(mentor,Salario))







