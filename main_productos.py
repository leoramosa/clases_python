from practica_productos import *

class productos_emp:
    def __init__(self, CODIGO, PROVEEDOR, PRODUCTOS, DESCRIPCION, PRECIO, STOCK, OBS):
        self.COD = CODIGO
        self.PRO = PROVEEDOR
        self.PROD = PRODUCTOS
        self.DESCR = DESCRIPCION
        self.PREC = PRECIO
        self.STOCK = STOCK
        self.OBS = OBS

    def __str__(self):
        return '{} {}'.format(self.COD, self.PRO)

print(Productos)







