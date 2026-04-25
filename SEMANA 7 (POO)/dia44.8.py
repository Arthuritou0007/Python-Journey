class Boxeador:
    def __init__(self, nombre_ingresado, peso_ingresado, fuerza_ingresado):
        self.nombre = nombre_ingresado
        self._peso = peso_ingresado
        self._fuerza = fuerza_ingresado

    def ver_peso(self):
        return self._peso
    
    def ver_fuerza(self):
        return self._fuerza

class Arbitro:
    def __init__(self):
        pass

    def pelea(self, boxeador1, boxeador2):
        nombre_boxeador1 = boxeador1.nombre
        nombre_boxeador2 = boxeador2.nombre

        peso_boxeador1 = boxeador1.ver_peso()
        peso_boxeador2 = boxeador2.ver_peso()

        fuerza_boxeador1 = boxeador1.ver_fuerza()
        fuerza_boxeador2 = boxeador2.ver_fuerza()

        diferencia = abs(peso_boxeador1 - peso_boxeador2)

        if diferencia > 5:
            raise ValueError(f"Error: ¡Pelea cancelada por reglamento! (Diferencia de {diferencia}kg)")
        elif fuerza_boxeador1 > fuerza_boxeador2:
            return f"¡{nombre_boxeador1} ha ganado la contienda, felicidades!"
        elif fuerza_boxeador2 > fuerza_boxeador1:
            return f"¡{nombre_boxeador2} ha ganado la contienda, felicidades!"


boxeadores = [Boxeador("Arthur", 69, 50), Boxeador("Lauti", 77, 40)]
arbitro = Arbitro()

print(arbitro.pelea(boxeadores[0], boxeadores[1]))