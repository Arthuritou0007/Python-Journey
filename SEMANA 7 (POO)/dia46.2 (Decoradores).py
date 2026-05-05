class Personaje:
    cantidad_personajes = 0

    def __init__(self, nombre_ingresado, vida_ingresada):
        self.nombre = nombre_ingresado
        self._vida = vida_ingresada
        Personaje.cantidad_personajes += 1

    @property
    def vida(self):
        return self._vida
    
    @vida.setter
    def vida(self, nuevo_valor): # Nuevo valor = resultado de la operación realizada en la línea 32
        if nuevo_valor < 0:
            self._vida = 0
        else:
            self._vida = nuevo_valor
    
    def __str__(self):
        return f"[{self.nombre}] - Vida: {self._vida}"
    
    def __repr__(self):
        return f"('{self.nombre}' | [V]{self._vida})"
    

    
gremio = [Personaje("Arthur", 200), Personaje("Mituri", 10), Personaje("Lauti", 30)]

print(Personaje.cantidad_personajes)
print(gremio[0].vida)
gremio[0].vida -= 250
print(gremio[0].vida)