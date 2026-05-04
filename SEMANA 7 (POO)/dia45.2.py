class Personaje:
    def __init__(self, nombre_ingresado, vida_ingresada):
        self.nombre = nombre_ingresado
        self._vida = vida_ingresada

    def ver_vida(self):
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

class Guerrero(Personaje):
    def __init__(self, nombre_ingresado, vida_ingresada, armadura_ingresada):
        super().__init__(nombre_ingresado, vida_ingresada)
        self.armadura = armadura_ingresada

    def modificar_vida(self, cantidad, opcion):
        if opcion == "restar":
            cantidad = cantidad - self.armadura
            if cantidad <= 0:
                cantidad = 0
            else:
                super().modificar_vida(cantidad, opcion)

class Mago(Personaje):
    def __init__(self, nombre_ingresado, vida_ingresada, poder_magico_ingresado):
        super().__init__(nombre_ingresado, vida_ingresada)
        self.poder_magico = poder_magico_ingresado

    def __str__(self):
        return super().__str__() + f" | Poder Mágico: {self.poder_magico}"
    
    def __repr__(self):
        return f"('{self.nombre}' | [V]{self._vida} | [PM]{self.poder_magico})"
    
gremio = [Mago("Mituri", 70, 90), Guerrero("Arthur", 100, 15)]

print("Presentando al gremio:")
for i in gremio:
    print(i)


print("¡Ha caído una lluvia de flechas sobre el gremio!")
for lluvia in gremio:
    lluvia.modificar_vida(10, "restar")
print(gremio)

print("¡Un aliado del clan de los magos ha lanzado una pócima de curación!")
for pocion in gremio:
    if isinstance(pocion, Mago):
        pocion.modificar_vida(20, "sumar")
print(gremio)

print("¡Resultado de la contienda!")
for i in gremio:
    print(i)