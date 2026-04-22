class Producto:
    def __init__(self, nombre_ingresado, precio_ingresado):
        self.nombre = nombre_ingresado
        self._precio = precio_ingresado

    def ver_precio(self):
        return self._precio

class Carrito:
    def __init__(self):
        self.contenido = []

    def agregar(self, producto):
        self.contenido.append(producto)

    def cobrar(self):
        contador = 0
        for i in self.contenido:
            contador = contador + i.ver_precio()
        return f"Su total a pagar es: ${contador}"

    
            
productos = [Producto("Manzana", 1000), Producto("Cereales", 500), Producto("Café", 600)]

chango_1 = Carrito()

chango_1.agregar(productos[0])
chango_1.agregar(productos[2])

print(chango_1.cobrar())