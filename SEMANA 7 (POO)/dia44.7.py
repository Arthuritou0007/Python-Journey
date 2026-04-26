class Cafetera:
    def __init__(self):
        self.agua = 1000
        self.cafe = 500

    def ver_contenido(self):
        return f"Agua: {self.agua}ml\nCafé: {self.cafe}g"
    
    def recargar_cafe(self):
        print("1. Café\n2. Agua")
        try:
            elección = int(input("Escoge qué quieres recargar: "))
        except ValueError:
            print("Error: Escoge una opción correcta")
            return
        if elección == 1:
            try:
                cantidad = int(input("Ingresa la cantidad de gramos de café que quieres recargar a la cafetera: "))
            except ValueError:
                print("Error: Ingresa un número válido")
            self.cafe = self.cafe + cantidad
            print("¡Cafetera recargada con éxito!")
            print(self.ver_contenido())
        elif elección == 2:
            try:
                cantidad = int(input("Ingresa la cantidad de ml de agua que quieres recargar a la cafetera: "))
            except ValueError:
                print("Error: Ingresa un número válido")
            self.agua = self.agua + cantidad
            print("¡Cafetera recargada con éxito!")
            print(self.ver_contenido())
        else:
            print("Error: Ingrese un número válido")


    def hacer_espresso(self):
        if self.agua < 50:
            agua_faltante = 50 - self.agua
            return f"No hay agua suficiente para realizar el espresso\nAgua faltante: {agua_faltante}ml"
        elif self.cafe < 20:
            cafe_faltante = 20 - self.cafe
            return f"No hay café suficiente para realizar el espresso\nAgua faltante: {cafe_faltante}g"
        else:
            self.agua = self.agua - 50
            self.cafe = self.cafe - 20
            return f"Has hecho un espresso exitosamente\nAgua restante: {self.agua}ml\nCafé restante: {self.cafe}g"
    
    def hacer_americano(self):
        if self.agua < 200:
            agua_faltante = 200 - self.agua
            return f"No hay agua suficiente para realizar el americano\nAgua faltante: {agua_faltante}ml"
        elif self.cafe < 15:
            cafe_faltante = 15 - self.cafe
            return f"No hay café suficiente para realizar el americano\nCafe faltante: {cafe_faltante}g"
        else:
            self.agua = self.agua - 200
            self.cafe = self.cafe - 15
            return f"Has hecho un americano exitosamente\nAgua restante: {self.agua}ml\nCafé restante: {self.cafe}g"
    
cafetera1 = Cafetera()

while True:
    print(cafetera1.ver_contenido())
    print("¿Qué te gustaría tomar hoy?\n1. Espresso\n2. Americano\n3. Recargar cafetera")
    try:
        eleccion = int(input("Ingrese su elección: "))
    except ValueError:
        print("Error: Ingrese un número válido")
        continue
    if eleccion == 1:
        print(cafetera1.hacer_espresso())
    elif eleccion == 2:
        print(cafetera1.hacer_americano())
    elif eleccion == 3:
        cafetera1.recargar_cafe()
    else:
        print("Error: Ingrese un número válido")


