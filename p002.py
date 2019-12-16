
class Cliente:
    def __init__(self, dni, nombre, apellidos):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos
    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellidos)
class Empresa:
    def __init__(self, clientes=[]):
        self.clientes = clientes
    def mostrar_cliente(self, dni=None):
        for c in self.clientes:
            if c.dni == dni:   
                print(c)
                return
        print("Cliente no existe")
Cliente1 = Cliente(nombre="Hector", dni="10210902", apellidos="Gomez")
Cliente2 = Cliente(nombre="Maria", dni="10210903", apellidos="Flores")
Cliente3 = Cliente(nombre="Raul", dni="10210904", apellidos="Rivas")
Cliente4 = Cliente(nombre="luis", dni="10210905", apellidos="Ruiz")
empresa = Empresa(clientes=[Cliente1, Cliente2, Cliente3, Cliente4])
empresa.mostrar_cliente("10210902")