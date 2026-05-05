class CuentaGoblin:
    def __init__(self, titular_ingresado, saldo_ingresado):
        self.titular = titular_ingresado
        self._saldo = saldo_ingresado

    @property
    def saldo(self):
        return self._saldo
    
    def extraer_oro(self, cantidad):
        if cantidad > self._saldo:
            print("¡Tramposo! El banco te ha cobrado una multa de 5 chelines.")
            self._saldo -= 5
            if self._saldo < 0:
                self._saldo = 0
            print(f"Saldo actual: {self.saldo}")
        else:
            self._saldo -= cantidad
            print(f"Retiro de dinero exitoso.\nSaldo actual: {self.saldo}")

banco = [CuentaGoblin("Michelo", 2), CuentaGoblin("Juan", 300)]

banco[0].extraer_oro(300)
banco[1].extraer_oro(150)