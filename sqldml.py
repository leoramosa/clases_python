import sqlite3
import os
import time
from colorama import Fore, Back, Style
bd = sqlite3.connect("tpv.db")
cursor = bd.cursor()
resp = ""
def cargarinventario():
    try:
        productos = [
            """
            INSERT INTO productos (codigo,nombre,precio,estado,codcat,barra)
            values ("PROD01","PIZZA DE POLLO",28.9,"1","1","10210902"),
            ("PROD02","PIZZA A LO PAOLO",22.9,"1","1","10210903"), 
            ("PROD03","PIZZA DE QUEZO",18.9,"1","1","10210904"), 
            ("PROD04","PIZZA VEGETARIANA",17.9,"1","1","10210905"), 
            ("PROD05","PIZZA  DE CARNE",12.9,"1","1","10210906"), 
            ("PROD06","PIZZA DE FRUTA",15.9,"1","1","10210907"),
            ("PROD07","GUARANA",9,"1","2","10210908")
          """
        ]
        for sentencia in productos:
            cursor.execute(sentencia)
            bd.commit()
        print("Productos Insertados correctamente")
    except sqlite3.OperationalError as error:
        print("Este el error:", error)
def listar():
    try:
        sentencia = "SELECT nombre,precio,estado,codcat from productos"
        cursor.execute(sentencia)
        productos = cursor.fetchall()
        print("+{:-<50}+{:-<20}+{:-<10}+{:-<10}+".format("", "", "", ""))
        print("|{:<50}|{:<20}|{:<10}|{:<10}|".format("Nombre", "Precio", "Estado", "Categoria"))
        print("+{:-<50}+{:-<20}+{:-<10}+{:-<10}+".format("", "", "", ""))
        for nombre, precio, estado, codcat in productos:
            print("|{:^50}|{:^20}|{:^10}|{:^10}|".format(nombre, precio, estado, codcat))
        print("+{:-<50}+{:-<20}+{:-<10}+{:-<10}+".format("", "", "", ""))
    except sqlite3.OperationalError as error:
        print("Este el error:", error)
def buscar():
    try:
        busqueda = input("Ingrese o pistole el codigo de barra>")
        sentencia = "SELECT nombre,precio,estado,codcat from productos where barra" + "'" + busqueda + "'"
        cursor.execute(sentencia)
        productos = cursor.fetchall()
        print(Style.DIM+"+{:-<50}+{:-<20}+{:-<10}+{:-<10}+".format("", "", "", ""))
        print(Fore.RED+"|{:<50}|{:<20}|{:<10}|{:<10}|".format("Nombre", "Precio", "Estado", "Categoria"))
        print("+{:-<50}+{:-<20}+{:-<10}+{:-<10}+".format("", "", "", ""))
        for nombre, precio, estado, codcat in productos:
            print("|{:^50}|{:^20}|{:^10}|{:^10}|".format(nombre, precio, estado, codcat))
        print("+{:-<50}+{:-<20}+{:-<10}+{:-<10}+".format("", "", "", ""))
    except sqlite3.OperationalError as error:
        print("Este el error:", error)
def menuprincipal():
    opc = "0"
    print("--Pizza Joan WELCOME--")
    print("1.-Cargar de Inventario")
    print("2.-Listado de Productos")
    print("3.-Busqueda de Productos")
    opc = input("Elija Una Opcion:")
    if opc == "1":
        cargarinventario()
    elif opc == "2":
        listar()
    elif opc == "3":
        buscar()
    else:
        print("Opcion No Existe")
while resp != 'N':
    menuprincipal()
    resp = input("¿Desea Continuar:").upper()
    os.system('cls')