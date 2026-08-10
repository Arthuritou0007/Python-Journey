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
        self.peso = peso
        self.categoria = determinar_categoria(peso)
    
    def __str__(self):
        return f"**BOXEADOR** Boxeador: {self.nombre} | DNI: {self.DNI} | Categoría: {self.categoria}"

class Federación:
    def __init__(self):
        self.padron = []

    def emitir_licencia(self, afiliado):
        self.padron.append(afiliado)

    def buscar_por_dni(self, dni):
        for i in self.padron:
            if i.DNI == dni:
                print(i)
                break
        else:
            print("No se encontró ningún licenciado registrado con ese DNI")

    def actualizar_peso(self, dni, nuevo_peso):
        for i in self.padron:
            if isinstance(i, Pugil):
                if i.DNI == dni:
                    i.peso = nuevo_peso
                    i.categoria = determinar_categoria(nuevo_peso)
                    break
        else:
            print("No se encontró a ningún boxeador con ese DNI")

    def cancelar_licencia(self, dni):
        for i in self.padron:
            if i.DNI == dni:
                print(f"La licencia de '{i.nombre}' ha sido eliminada correctamente")
                self.padron.remove(i)
                break
        else:
            print("No se encontró ningún licenciado registrado con ese DNI")