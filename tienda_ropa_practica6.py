nom = input("Ingrese el nombre del comprador: ")
nacion = int(input("Indique caracteristica de nacionalidad (1/2): "))
genero = input("Indique el genero del produto (h/m): ")
talla = input('Indique la talla del producto (n,j.a): ')
cant = int(input("Ingrese la cantiad de productos comprados: "))
punit = float(input("Ingrese el importe unitario de los productos: "))
importe = cant * punit
cond = str(nacion) + genero + talla
print(cond)
if cond == '1hn' or cond == '2mn':
    desc = importe * 0.05
    print('El desc a aplicar es 5%, equivale a: {}'.format(desc))
elif cond == '2hn' or cond == '1mn':
    desc = importe * 0.04
    print('El desc a aplicar es 4%, equivale a: {}'.format(desc))
elif cond == '1hj' or cond == '2mj':
    desc = importe * 0.07
    print('El desc a aplicar es 7%, equivale a: {}'.format(desc))
elif cond == '1mj' or cond == '2hj':
    desc = importe * 0.09
    print('El desc a aplicar es 9%, equivale a: {}'.format(desc))
elif cond == '1ha' or cond == '2ma':
    desc = importe * 0.1
    print('El desc a aplicar es 10%, equivale a: {}'.format(desc))
elif cond == '2ha' or cond == '1ma':
    desc = importe * 0.12
    print('El desc a aplicar es 12%, equivale a: {}'.format(desc))
pago = importe - desc
print('El importe a pagar es: {}'.format(pago))