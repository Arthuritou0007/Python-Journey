class Producto:
    def __init__(self, nombre_ingresado):
        self.nombre = nombre_ingresado
        self._precio = 1000

    def __str__(self):
        return f"Producto: {self.nombre}, Precio: ${self._precio}"
    
    def __repr__(self):
        return f"{self.nombre}: ${self._precio}"
    

inventario = [Producto("Papas"), Producto("Mandioca"), Producto("Zanahoria")]

print(inventario)
print(inventario[1])