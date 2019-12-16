# Es la estructura o la plantilla de un objeto
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

jugador1 = Jugador(200, 80, 100, "Pedro")
jugador2 = Jugador(200, 180, 120, "Carlos")
armando = Jugador(300, 20, 120, "Armando")
leonardo = Jugador(2000,2000,2000,"leonardo")

#jugador1.pase_corto()
#jugador2.pase_corto()
#armando.pase_corto()
#leonardo.pase_corto()
print(leonardo)