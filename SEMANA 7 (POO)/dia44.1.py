class Factura:
    def __init__(self, nombre_ingresado, monto_ingresado):
        self.cliente = nombre_ingresado
        self._monto = monto_ingresado

    def __repr__(self):
        return f"Factura N°23(CLIENTE={self.cliente} MONTO={self._monto})" #La verdad que haría un sistema que cuente las facturas y las enumere pero quiero entender bieneésto y tengo que ir a laburar XD
    
    def __str__(self):
        return f"*** TICKET DE COMPRA *** Cliente: {self.cliente} | A pagar: {self._monto}"
    
clientes = [Factura("Arthur", 1000), Factura("Miguelito", 2400), Factura("Juan", 10)]

print(clientes[1])
print(clientes)