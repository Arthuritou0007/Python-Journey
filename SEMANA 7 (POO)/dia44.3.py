class Turno:
    turno = 0

    def __init__(self, cliente_ingresado): # Por no ponerle la "t" al init se me rompió todo el código :v
        self.cliente = cliente_ingresado
        Turno.turno = Turno.turno + 1
        self.ticket = Turno.turno

    def __str__(self):
        return f"Cliente: {self.cliente} | Turno: {self.ticket}"
    
    def __repr__(self):
        return f"Factura N°{self.ticket}(CLIENTE={self.cliente})"
    
clientes = [Turno("A"), Turno("B"), Turno("C")]

print(clientes[1])
print(clientes)