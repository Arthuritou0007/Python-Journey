class Licencia:

    contador_licencias = 0

    def __init__(self, nombre, DNI):
        Licencia.contador_licencias = Licencia.contador_licencias + 1
        self.nombre = nombre
        self._DNI = DNI
        self.numero_licencia = Licencia.contador_licencias

    @property
    def DNI(self):
        return self._DNI
    
    def __str__(self):
        return f"** LICENCIA DE BOXEADOR AMATEUR ** Boxeador: {self.nombre} | DNI: {self.DNI}"
    
    def __repr__(self):
        return f"Licencia N°{self.numero_licencia}(BOXEADOR={self.nombre} DNI={self.DNI})"
    
licenciados = [Licencia("Arthur", 46730690), Licencia("Florencia", 44841669), Licencia("Gonza", 44841669), Licencia("Fran", 44841669), Licencia("Lautaro", 44841669)]

print(licenciados)
print(f"\n{licenciados[3]}")