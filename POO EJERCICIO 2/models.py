class Pedido:
    def __init__(self, comensal, mesa):
        self.comensal = comensal
        self.mesa = mesa
        self.productos = []

    def agregar_producto(self, pedido):
        for i in menu:
            if i["Producto"] == pedido:
                self.productos.append(i)

    def calcular_total(self):
        contador = 0
        for i in self.productos:
            contador += i["Valor"]
        return contador

    def to_dict(self):
        return {
            "comensal": self.comensal,
            "mesa": self.mesa,
            "productos": self.productos
        }


menu = [
    {"Producto": "Hamburguesa con papas", "Valor": 5000},
    {"Producto": "Porción de papas", "Valor": 2500},
    {"Producto": "Gaseosa", "Valor": 3000}
]