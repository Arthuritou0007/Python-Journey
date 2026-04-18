class Usuario:
    def __init__(self, edad_ingresada, direccion_ingresada, nombre_ingresado):
        self.edad = edad_ingresada
        self.direccion = direccion_ingresada
        self.nombre = nombre_ingresado
    
    def cumplir_años(self):
        self.edad = self.edad + 1

        return f"¡Feliz cumpleaños! ¡Has cumplido {self.edad} años!"
    
arthur = Usuario(20, "Las Violetas", "Arthur")

print(arthur.cumplir_años())