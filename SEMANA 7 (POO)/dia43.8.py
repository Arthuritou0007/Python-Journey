class Boxeador:
    def __init__(self):
        self._energia = 100

    
    def entrenar(self):
        if self._energia < 15:
            raise ValueError("Error: No tienes energía para realizar esta acción")
        self._energia = self._energia - 15
        return f"¡Realizaste un entrenamiento y gastaste 15 de energía!"
    def jab(self):
        if self._energia < 15:
            raise ValueError("Error: No tienes energía para realizar esta acción")
        self._energia = self._energia - 20
        return f"¡Lanzaste un jab y usaste 20 de energía!"
    def directo(self):
        if self._energia < 15:
            raise ValueError("Error: No tienes energía para realizar esta acción")
        self._energia = self._energia - 30
        return f"¡Lanzaste un directo y usaste 30 de energía!"
    
    def mostrar_energia(self):
        return f"Energía restante {self._energia}"
    
    

    
arthur = Boxeador()

while True:
    print("Escoge tu opción")
    print("1. Entrenar (Coste de energía: 15)")
    print("2. Lanzar jab (Coste de energía: 20)")
    print("3. Lanzar directo (Coste de energía: 30)")
    print(f"{arthur.mostrar_energia()}")
    eleccion = int(input("Ingrese aquí su elección: "))

    if eleccion == 1:
        print(arthur.entrenar())
    if eleccion == 2:
        print(arthur.jab())
    if eleccion == 3:
        print(arthur.directo())