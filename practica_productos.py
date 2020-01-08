import sqlite3
conexion = sqlite3.connect("Productos.db")
cursor = conexion.cursor()
#resp = ""


def listar():
    try:
        sentencia = "SELECT COD, PROVEEDOR, PRODUCTOS, DESCRIPCION, PRECIO, STOCK, OBS from Productos"
        cursor.execute(sentencia)
        Productos = cursor.fetchall()
        print("+{:-<10}+{:-<20}+{:-<20}+{:-<40}+{:-<10}+{:-<10}+{:-<10}+".format("", "", "", "", "", "", ""))
        print("|{:<10}|{:<20}|{:<20}|{:<40}|{:<10}|{:<10}|{:<10}|".format("COD", "PROVEEDOR", "PRODUCTOS", "DESCRIPCION","PRECIO","STOCK","OBS"))
        print("+{:-<10}+{:-<20}+{:-<20}+{:-<40}+{:-<10}+{:-<10}+{:-<10}+".format("", "", "", "","","",""))
        for COD, PROVEEDOR, PRODUCTOS, DESCRIPCION, PRECIO, STOCK, OBS in Productos:
            print("|{:^10}|{:^20}|{:^20}|{:^40}|{:^10}|{:^10}|{:^10}|".format(COD, PROVEEDOR, PRODUCTOS, DESCRIPCION ,PRECIO , STOCK , OBS))
        print("+{:-<10}+{:-<20}+{:-<20}+{:-<40}+{:-<10}+{:-<10}+{:-<10}+".format("", "", "", "","","",""))

    except sqlite3.OperationalError as error:
        print("Este el error:", error)

#listar()