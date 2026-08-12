class Mascota:
    def __init__(self, nombre, animal, dueño, motivo):
        self.nombre = nombre
        self.animal = animal
        self.dueño = dueño
        self.motivo = motivo

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "animal": self.animal,
            "dueño": self.dueño,
            "motivo": self.motivo
        }