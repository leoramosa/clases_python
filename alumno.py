class Alumno:
    def __init__(self, nombre, promedio):
        self.nom = nombre
        self.prom = promedio
    def __str__(self):
        return self.nom

    def estado(self):
        if self.prom > 10.5:
            print("alumno aprobado")
        else:
            print("alumno desaporbado")