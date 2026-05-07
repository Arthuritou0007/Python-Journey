class Escudo:
    escudos_forjados = 0

    def __init__(self, nombre_ingresado):
        self.nombre = nombre_ingresado
        self._durabilidad = 10
        Escudo.escudos_forjados += 1

    @property
    def durabilidad(self):
        return self._durabilidad
    
    def recibir_golpe(self, daño):
        self._durabilidad -= daño
        print(f"¡El escudo recibió un golpe de {daño} de daño! Durabilidad restante: {self.durabilidad}")
        if self._durabilidad <= 0:
            self._durabilidad = 0
            print("¡El escudo se rompió!")

escudo = Escudo("Escudo")

while True:
    try:
        escudo.recibir_golpe(int(input("Cantidad de daño: ")))
    except ValueError:
        print("Error: Ingrese un dato válido.")
    
    if escudo.durabilidad == 0:
        break