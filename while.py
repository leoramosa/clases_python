edad = 0
while edad <18: #condicion logica = valor true o valor false
    edad = edad +1
    if edad % 2 == 0:
        #cuando se cumpla esta condicion no realizara nada
        continue # se puede utlizar break
    print("tu edad actual es", edad)