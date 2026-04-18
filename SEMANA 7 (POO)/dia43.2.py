class Boxeador:
    def __init__(self, peso_ingresado, edad_ingresada, peleas_ingresadas, estatura_ingresada):
        self.peso = peso_ingresado
        self.edad = edad_ingresada
        self.peleas = peleas_ingresadas
        self.estatura = estatura_ingresada

    def tirar_jab(self):
        return "¡Pum! Jab rápido."
    

arthur = Boxeador(69, 20, 0, 1.69)
lauti = Boxeador(67, 19, 7, 1.78)

print(arthur.peso)
print(lauti.peso)

lauti.peso = lauti.peso + 2
arthur.peso = arthur.peso + 2

print(arthur.peso)
print(lauti.peso)