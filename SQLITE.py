import sqlite3
#conectarse a la bd codiGo , lo crea
conexion = sqlite3.connect("codiGo")
#administra la BD
cursor = conexion.cursor()
def creartabla():
    try:
        cursor.execute("CREATE TABLE usuarios(nombre TEXT, edad INTEGER,email TEXT, dni NUMERIC, foto BLOB, salario REAL)")
        #Guardar la tabla en la BD
        conexion.commit()
        #Cierre la conexion
        conexion.close()
    except sqlite3.OperationalError as error:
        print("Error al crear la talba", error)

def insertar():
   #cursor.execute("INSERT INTO usuarios values "
                   #"('Wilber',19,'wilber@codig.pe',63537288883,'',5400.00)")
    #conexion.commit()

    cursor.execute("INSERT INTO usuarios (nombre,edad) values "
                   "('Wilber' ,19)")
    conexion.commit()     

def insertargrupo():
    usuarios  = [
        ('maria', 25, 'mariag@codigo.pe', 32849329493),
        ('leo', 25, 'mariag@codigo.pe', 32849329493),
        ('martin', 25, 'mariag@codigo.pe', 32849329493),
        ('roxana', 25, 'mariag@codigo.pe', 32849329493),
        ('martha', 25, 'mariag@codigo.pe', 32849329493)
    ]
    cursor.executemany("INSERT INTO usuarios(nombre,edad,email,dni) values (?,?,?,?)", usuarios )
    conexion.commit()

insertargrupo()

#creartabla() se oculta porque ya no necesito la funcion crear tabla
#insertar()