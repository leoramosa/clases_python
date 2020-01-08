from productos_tabla import *
pm = Productos_Metodos()
def registrar_productos():
    print("Registrando productos")
    codigo = input("El Codigo:")
    nombre = input("El Nombre:")
    prov = input("El Proveedor:")
    categoria = input("La Categoria:")
    pre = input("La Presentacion:")
    precio = input("El Precio:")
    stock = input("El Stock:")
    estado = input("El Estado:")
    nuevoproducto = Productos(codigo, nombre, prov, categoria, pre, precio, stock, estado)
    pm.agregar(nuevoproducto)
    pm.insertar_tabla()
def mostrar_productos():
    print(pm)
def menu():
    op = 0
    salir = 3
    while op != salir:
        print("Menu")
        print("1.-Registrar Productos")
        print("2.-Listar Productos")
        print("3.-Salir")
        op = input("Digite la opcion:")
        if op == "1":
            registrar_productos()
        elif op == "2":
            mostrar_productos()
        else:
            exit()
menu()





