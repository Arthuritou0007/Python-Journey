class Deposito:
    def __init__(self):
        self._inventario = {}


    def ingresar_mercaderia(self, producto, cantidad):
        if cantidad < 0:
            raise ValueError("Error: No se admiten números negativos.")
        
        existe = 0

        for i in self._inventario:
            if i == producto:
                existe = True
                break
            else:
                existe = False

        if existe == False:
            self._inventario[producto] = cantidad
        else:
            self._inventario[producto] = self._inventario[producto] + cantidad

    def mirar_mercaderia(self):
        return f"{self._inventario}"
    
inventario = Deposito()

while True:

    producto = input("Ingrese el nombre del producto: ")
    try:
        cantidad = int(input("Ingrese la cantidad: "))
    except ValueError:
        print("Error: Ingrese un dato válido.")
        continue

    inventario.ingresar_mercaderia(producto, cantidad)
    print(inventario.mirar_mercaderia())

    print("¿Quieres registrar un nuevo producto al inventario?")
    print("1. Sí")
    print("2. No")
    try:
        eleccion = int(input("Ingrese su respuesta: "))
    except ValueError:
        print("Ingrese una opción válida")

    if eleccion == 1:
        continue
    if eleccion == 2:
        print(f"{inventario.mirar_mercaderia}")
        break