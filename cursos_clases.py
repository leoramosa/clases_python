class Cursos:
    def __init__(self, nombre, precio,cara):
        self.nom = nombre
        self.pre = precio
        self.car = cara

    def __str__(self):
        return self.nom

    def curso_caro(self):
        if self.pre>1000:
            print('curso es caro')
        else:
            print('curso varatito')

curso1 = Cursos('Flask', 800,'MicroFramework Python')
curso2 = Cursos('Django', 800,'Framework Python')

print(curso1)
print(curso2)
