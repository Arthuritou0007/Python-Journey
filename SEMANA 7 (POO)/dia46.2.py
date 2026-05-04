class Personaje:
    cantidad_personajes = 0

    def __init__(self, nombre_ingresado, vida_ingresada):
        self.nombre = nombre_ingresado
        self._vida = vida_ingresada
        Personaje.cantidad_personajes += 1

    @property
    def vida(self):
        return self._vida
    
    def modificar_vida(self, cantidad, opcion):
        if opcion == "restar":
            self._vida = self._vida - cantidad
        elif opcion == "sumar":
            self._vida = self._vida + cantidad
        else:
            print("¡Ingrese una opción válida!")
            return

    def __str__(self):
        return f"[{self.nombre}] - Vida: {self._vida}"
    
    def __repr__(self):
        return f"('{self.nombre}' | [V]{self._vida})"
    
gremio = [Personaje("Arthur", 200), Personaje("Mituri", 10), Personaje("Lauti", 30)]

print(Personaje.cantidad_personajes)
print(gremio[0].vida)