class Vehiculo:
    def __init__(self, nombre_ingresado):
        self.nombre = nombre_ingresado
        self._combustible = 100

    def viajar(self, distancia):
        self._combustible -= distancia

    def __str__(self):
        return f"{self.nombre} | Combustible: {self._combustible}"
    
    def __repr__(self):
        return f"({self.nombre} | [F]{self._combustible})"
    
class Submarino(Vehiculo):
    def __init__(self, nombre_ingresado):
        super().__init__(nombre_ingresado)
        self._costo_inmersion = 10

    def viajar(self, distancia):
        distancia += self._costo_inmersion
        super().viajar(distancia)

class Nave(Vehiculo):
    def __init__(self, nombre_ingresado):
        super().__init__(nombre_ingresado)

    def viajar(self, distancia):
        distancia = distancia * 2
        super().viajar(distancia)

vehiculos = [Submarino("Maira"), Nave("Titán")]

vehiculos[0].viajar(50)
vehiculos[1].viajar(30)

print(vehiculos)