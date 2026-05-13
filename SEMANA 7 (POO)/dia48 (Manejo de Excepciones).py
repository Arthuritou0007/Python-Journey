class Flecha:
    def __init__(self, daño, nombre):
        self.daño = daño
        self.nombre = nombre
    
    def __str__(self):
        return self.nombre

class Carcaj:
    def __init__(self):
        self.municion = []

    def guardar_flecha(self, flecha):
        self.municion.append(flecha)

class Arquero:
    def __init__(self, nombre):
        self.nombre = nombre
        self.espalda = Carcaj()
    
    def disparar(self):
        try:
            flecha_disparada = self.espalda.municion.pop()

            print(f"¡Lanzaste {flecha_disparada}! Causaste {flecha_disparada.daño} de daño.")
        except IndexError:
            print("Error: Tu Carcaj se quedó sin flechas.")


flecha_fuego = Flecha(20, "Flecha de Fuego")
flecha_normal = Flecha(30, "Flecha Normal")
Arthur = Arquero("Arthur")

Arthur.espalda.guardar_flecha(flecha_fuego)
Arthur.espalda.guardar_flecha(flecha_normal)

Arthur.disparar()
Arthur.disparar()
Arthur.disparar()