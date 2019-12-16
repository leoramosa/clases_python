class Cuenta:

	# por ahora nuestra clase sólo tiene un atributo.
	def __init__(self, valor):
		self.cantidad = valor

class Jugador:
    # Es el constructor de la clase
    # tres Atributos
    def __init__(self, vel, pre, ene, nom):
        self.nombre = nom
        self.velocidad = vel
        self.precision = pre
        self.energia = ene
    #ejemplo de imprimir atributos
    #def __str__(self):
        #return self.nombre

    def __str__(self):
        return "caracteristicas {},{},{}".format(self.nombre, self.velocidad, self.precision)

    # esto es un metodo
    def tirar_al_arco(self):
        print(self.nombre, "Tiene de energia:", self.energia)
    def pase_corto(self):
        if self.precision > 100:
            print(self.nombre, "Tiene una pase corto Bueno")
        else:
            print(self.nombre, "Tiene un pase corto NO MUY Bueno")
    def pase_centro(self):
        print(self.nombre, "Tiene de energia:", self.energia)