class Billetera:
    def __init__(self, saldo_ingresado):
        self._saldo = saldo_ingresado
        self._historial_gastos = []

    def gastar(self, gasto):
        if gasto > self._saldo:
            raise ValueError("Error: No tienes dinero suficiente para realizar ésta compra.")
        else:
            self._saldo = self._saldo - gasto
            self._historial_gastos.append(gasto)

    def consultar_saldo(self):
        return self._saldo


billetera_arthur = Billetera(1000)

tienda = [
    {"articulo": "Coca", "precio": 200},
    {"articulo": "Guantes nuevos", "precio": 1500}
]

while True:
    print("¿Qué artículo quieres comprar?")
    print(f"1. {tienda[0]["articulo"]} {tienda[0]["precio"]}")
    print(f"2. {tienda[1]["articulo"]} {tienda[1]["precio"]}")
    print(f"El dinero en tu cuenta es de: ${billetera_arthur.consultar_saldo()}")
    try:
        elección = int(input("Ingrese aquí su respuesta: "))
    except ValueError:
        print("Ingrese una opción válida")
        continue
    if elección == 1:
        billetera_arthur.gastar(tienda[0]["precio"])
        print(f"Compra realizada con éxito. Tu compra se ha agregado a tu historial de gastos.")
        print(f"Tu nuevo saldo es de: ${billetera_arthur.consultar_saldo()}")
    elif elección == 2:
        billetera_arthur.gastar(tienda[1]["precio"])
        print(f"Compra realizada con éxito. Tu compra se ha agregado a tu historial de gastos.")
        print(f"Tu nuevo saldo es de: ${billetera_arthur.consultar_saldo()}")
    else:
        print("Ingrese una opción válida")