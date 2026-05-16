class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self._precio = precio
        self.cantidad = cantidad

    @property
    def precio(self):
        return self._precio

    def __str__(self):
        return f"Producto: {self.nombre} | Bultos: {self.cantidad} | Precio: {self.precio} "

class Verdura(Producto):
    def __init__(self, nombre, precio, cantidad, kilos):
        super().__init__(nombre, precio, cantidad)      
        self.kilos = kilos

    def __str__(self):
        return super().__str__() + f"| Kilos: {self.kilos}"

class Dietetica(Producto):
    def __init__(self, nombre, precio, cantidad, gramos):
        super().__init__(nombre, precio, cantidad)
        self.gramos = gramos

    def __str__(self):
        return super().__str__() + f"| Gramos: {self.gramos}"

class Local:
    def __init__(self):
        self.inventario = []

    def recibir_mercadería(self, producto):
        self.inventario.append(producto)

    def mostrar_inventario(self):
        contador_verduras = 0
        contador_dietetica = 0
        for i in self.inventario:
            if isinstance(i, Verdura):
                contador_verduras += 1
        for i in self.inventario:
            if isinstance(i, Dietetica):
                contador_dietetica += 1
        print(f"Productos de dietética registrados: {contador_dietetica}\nProductos de verdulería registrados: {contador_verduras}")
        print("¿Cuál lista deseas ver?\n1. Dietetica\n2. Verdulería")
        eleccion = int(input("Ingrese aquí su respuesta:"))

frutimas = Local()

frutimas.recibir_mercadería(Verdura("Manzana", 1200, 2, 15))
frutimas.mostrar_inventario()