class Escudo:
    def __init__(self, nombre, defensa, durabilidad):
        self.nombre = nombre
        self.defensa = defensa
        self.durabilidad = durabilidad

    def recibir_daño(self, daño_entrante):
        if daño_entrante < self.defensa:
            daño_total = 0
        else:
            daño_total = daño_entrante - self.defensa
        self.durabilidad -= daño_total
        print(f"¡El escudo recibió un golpe de {daño_total} daño! Durabilidad restante: {self.durabilidad}")
        if self.durabilidad <= 0:
            print("¡El escudo se ha roto!")

class Guerrero:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mano_izquierda = None

    def equipar_escudo(self, escudo_nuevo):
        self.mano_izquierda = escudo_nuevo

    def defender_ataque(self, daño_entrante):
        if self.mano_izquierda is not None:
            self.mano_izquierda.recibir_daño(daño_entrante)
        else:
            print(f"¡Recibiste de lleno un golpe de {daño_entrante} de daño por no tener escudo!")


arthur = Guerrero("Arthur")
escudo_roble = Escudo("Escudo de Roble", 15, 20)

arthur.equipar_escudo(escudo_roble)

arthur.defender_ataque(30)
arthur.defender_ataque(6)
arthur.defender_ataque(20)