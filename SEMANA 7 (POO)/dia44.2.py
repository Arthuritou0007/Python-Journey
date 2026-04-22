class Factura:

    contador_facturas = 0

    def __init__(self, nombre_ingresado, monto_ingresado):
        Factura.contador_facturas = Factura.contador_facturas + 1
        self.cliente = nombre_ingresado
        self._monto = monto_ingresado
        self.ticket = Factura.contador_facturas

    def __repr__(self):
        return f"Factura N°{self.ticket}(CLIENTE={self.cliente} MONTO={self._monto})"
    
    def __str__(self):
        return f"*** TICKET DE COMPRA *** Cliente: {self.cliente} | A pagar: {self._monto}"
    
clientes = [Factura("Arthur", 1000), Factura("Miguelito", 2400), Factura("Juan", 10)]

print(clientes[1])
print(clientes)