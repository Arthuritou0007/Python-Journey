class Personaje:
    def __init__(self, nombre_ingresado, vida_ingresada):
        self.nombre = nombre_ingresado
        self._vida = vida_ingresada

    @property
    def vida(self):
        return self._vida
    
    def modificar_vida(self, cantidad, opcion):
        if opcion == "restar":
            self._vida -= cantidad
            if self._vida < 0:
                self._vida = 0
        elif opcion == "sumar":
            self._vida += cantidad
        else:
            print("Ingrese una opción correcta")
            return

class Guerrero(Personaje):
    def __init__(self, nombre_ingresado, vida_ingresada):
        super().__init__(nombre_ingresado, vida_ingresada)
        self._armadura = 15

    @property
    def armadura(self):
        return self._armadura

    def modificar_vida(self, cantidad, opcion):
        if opcion == "restar": 
            if cantidad < self._armadura:
                cantidad = 0
            else:
                cantidad -= self._armadura
        return super().modificar_vida(cantidad, opcion)
    

gremio = [Personaje("Arthur", 200), Guerrero("Mituri", 250)]

print(gremio[1].vida)
gremio[1].modificar_vida(200, "restar")
print(gremio[1].vida)
gremio[1].modificar_vida(150, "sumar")
print(gremio[1].vida)
gremio[1].modificar_vida(10, "restar")
print(gremio[1].vida)