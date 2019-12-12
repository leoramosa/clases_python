print("===========================================")
nombre=input("Ingrese nombre: ")
direccion=input("Ingrese direccion: ")
telefono=input("Ingrese telefono: ")
cantidad_llamadas=int(input("Ingrese cantidad de llamadas al mes: "))
print("===========================================")
if cantidad_llamadas<=50:
    monto_a_pagar=0.5*cantidad_llamadas
elif cantidad_llamadas<=150:
    monto_a_pagar =(0.5*(50)) + (0.3*(cantidad_llamadas - 50))
elif cantidad_llamadas>150:
    monto_a_pagar = (0.5 * 50) + (0.3 * 100) + (0.6*(cantidad_llamadas-150))
print("===========================================")
print("Nombre: [{}]".format(nombre))
print("Direccion: [{}]".format(direccion))
print("Telefono: [{}]".format(telefono))
print("Importe a pagar: [{}]".format(monto_a_pagar))
print("===========================================")