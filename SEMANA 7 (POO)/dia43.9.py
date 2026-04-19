class Articulo:

    def __repr__(self):
        return f"{self.nombre}: ${self._precio}"

    def __init__(self, nombre_ingresado):
        self.nombre = nombre_ingresado
        self._precio = 2000

    def ver_precio(self): #getter
        return self._precio
    
    def cambiar_precio(self, precio_nuevo): #setter
        self._precio = precio_nuevo

productos = [Articulo("Nueces"), Articulo("Castañas"), Articulo("Almendras")]

for i in productos:
    precio_nuevo = i.ver_precio() * 1.20
    i.cambiar_precio(precio_nuevo)

print(productos)