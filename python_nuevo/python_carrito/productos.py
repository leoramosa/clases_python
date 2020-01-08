class Productos:
    def __init__(self, cod, nom, prov, cat, pres, pre, sto, est):
        self.codigo = cod
        self.nombre = nom
        self.proveedor = prov
        self.categoria = cat
        self.presentacion = pres
        self.precio = pre
        self.stock = sto
        self.estado = est
    def __str__(self):
        return '{}{}{}{}{}{}{}{}'.format(self.codigo, self.nombre, self.proveedor,
                                         self.categoria, self.presentacion, self.precio,
                                         self.stock, self.estado)
class Productos_Metodos:
    def __init__(self):
        self.productos = []
    def __str__(self):
        cadena = "Total de productos en stock" + str(len(self.productos))
        for producto in self.productos:
            cadena += "\n" + str(producto)
        return cadena
    def agregar(self, prod):
        self.productos.append(prod)