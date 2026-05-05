class Artefacto:
    valor_total_boveda = 0

    def __init__(self, nombre_ingresado, valor_ingresado):
        self.nombre = nombre_ingresado
        self._valor = valor_ingresado
        if self._valor < 0:
            self._valor = 0
            Artefacto.valor_total_boveda += 0
        else:
            Artefacto.valor_total_boveda += self._valor

    @property
    def valor(self):
        return self._valor
    

cofre = [Artefacto("Pistola", 200), Artefacto("Cuchillo Maldito", -200), Artefacto("Katana", 20)]

print(cofre[1].valor)
print(Artefacto.valor_total_boveda)