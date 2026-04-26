class Cuenta:
    def __init__(self, titular_ingresado):
        self._saldo = 10000
        self.titular = titular_ingresado

    def ver_dinero(self):
        return self._saldo

    def restar_dinero(self, cantidad):
        self._saldo = self._saldo - cantidad
        return self._saldo
    
    def sumar_dinero(self, cantidad):
        self._saldo = self._saldo + cantidad
        return self._saldo
    
    def __str__(self):
        return self.titular
    
class Banco:
    def __init__(self):
        pass

    def transferir(self, cuenta_origen, cuenta_destino, monto):
        if cuenta_origen.ver_dinero() < monto:
            raise ValueError(f"Error: Saldo insuficiente para realizar la transferencia.")
        else:
            cuenta_destino.sumar_dinero(monto)
            return f"Has transferido ${monto} a {cuenta_destino}.\nSaldo restante: {cuenta_origen.restar_dinero(monto)}."
        
banco_central = Banco()
usuarios = [Cuenta("Arthur"), Cuenta("Mituri")]

print(banco_central.transferir(usuarios[0], usuarios[1], 1000))