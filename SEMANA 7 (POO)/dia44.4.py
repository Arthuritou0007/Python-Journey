class Latas:
    def __init__(self):
        self._stock = 5
        self._precio = 1500

    def mostrar_stock(self):
        return f"Stock restante de latas: {self._stock}"

    def comprar(self, dinero_ingresado):
        self.ingreso = dinero_ingresado
        if self._stock == 0:
            raise ValueError("Error: Máquina vacía.")
        elif self.ingreso < self._precio:
            raise ValueError("Error: No tienes dinero suficiente.")
        else:
            self.ingreso = self.ingreso - self._precio
            self._stock = self._stock - 1
            return f"¡Has comprado una lata! Tu vuelto: {self.ingreso}"

Maquina = Latas()

print(Maquina.comprar(2000))    