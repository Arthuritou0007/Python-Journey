def determinar_categoria(peso):
    if peso <= 60:
        return "Medio"
    if peso <= 67:
        return "Welter"
    if peso > 67:
        return "Mediano"

class Licencia:

    contador_licencias = 0

    def __init__(self, nombre, DNI):
        Licencia.contador_licencias += 1
        self.nombre = nombre
        self._DNI = DNI
        self.numero_licencia = Licencia.contador_licencias

    @property
    def DNI(self):
        return self._DNI
    
    def __repr__(self):
        return f"Licencia N°{self.numero_licencia}(LICENCIADO={self.nombre} DNI={self.DNI})"

class Juez(Licencia):
    def __init__(self, nombre, DNI, rango):
        super().__init__(nombre, DNI)
        self.rango = rango
    
    def __str__(self):
        return f"**JURADO** Juez: {self.nombre} | DNI: {self.DNI} | Rango: {self.rango}"

class Pugil(Licencia):
    def __init__(self, nombre, DNI, peso):
        super().__init__(nombre, DNI)
        self.peso = determinar_categoria(peso)
    
    def __str__(self):
        return f"**BOXEADOR** Boxeador: {self.nombre} | DNI: {self.DNI} | Categoría: {self.peso}"

licenciados = [Juez("Pablo", 367289, "Provincial"), Pugil("Arthur", 6472388, 65), Juez("Pedro", 367289, "Nacional"), Pugil("Flor", 6472388, 49), Pugil("Wllter", 6472388, 760)]

print(licenciados)
print(f"\n{licenciados[1]}")
print(f"\n{licenciados[3]}")
print(f"\n{licenciados[4]}")