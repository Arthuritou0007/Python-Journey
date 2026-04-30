class Producto:
    def __init__(self, nombre_ingresado, precio_ingresado):
        self.nombre = nombre_ingresado
        self.precio = precio_ingresado

    def __str__(self):
        return f"{self.nombre} | {self.precio}"
    
    def  aplicar_descuento(self, porcentaje):
        self.precio = int(self.precio - (self.precio * porcentaje / 100))
    
class Limpieza(Producto):
    def __init__(self, nombre_ingresado, precio_ingresado, es_toxico):
        super().__init__(nombre_ingresado, precio_ingresado)

        self.es_toxico = es_toxico

    def __str__(self):
        if self.es_toxico == True:
            return super().__str__() + " (Es tóxico)"
        else:
            return super().__str__() + " (No es tóxico)"
        
    def aplicar_descuento(self, porcentaje):
        if porcentaje > 20:
            print("Error: Los productos de limpieza no pueden tener un descuento mayor al 20%.")
        else:
            super().aplicar_descuento(porcentaje)

class Fruta(Producto):
    def __init__(self, nombre_ingresado, precio_ingresado, dias_maduracion):
        super().__init__(nombre_ingresado, precio_ingresado)

        self.maduracion = dias_maduracion

    def __str__(self):
        return super().__str__() + f" (Madura en: {self.maduracion} días)"
    
inventario = [Fruta("Manzana", 200, 7), Limpieza("Lavandina", 1000, True), Fruta("Banana", 300, 4), Fruta("Mango", 2000, 3)]

for i in inventario:
    if isinstance(i, Fruta):
        i.aplicar_descuento(50)

for i in inventario:
    print(i)