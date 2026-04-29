class Personaje:
    def __init__(self, nombre_ingresado):
        self.nombre = nombre_ingresado
        self._mana = 50
        self._vida = 100

    def ver_vida(self):
        return self._vida
    
    def ver_mana(self):
        return self._mana
    
    def restar(self, cantidad, opcion):
        if opcion == "mana":
            self._mana = self._mana - cantidad
        elif opcion == "vida":
            self._vida = self._vida - cantidad
        else:
            raise ValueError("Error: Ingrese una opciòn correcta")
        
    def sumar(self, cantidad, opcion):
        if opcion == "mana":
            self._mana = self._mana + cantidad
        elif opcion == "vida":
            self._vida = self._vida + cantidad
        else:
            raise ValueError("Error: Ingrese una opciòn correcta")
        
    def __str__(self):
        return f"{self.nombre} - Vida: {self.ver_vida()} | Maná: {self.ver_mana()}"
    
class Arena:
    def __init__(self):
        pass

    def lanzar_hechizo(self, atacante, defensor):
        if atacante is defensor:
            raise ValueError("Error: No puedes golpearte a ti mismo.")
        else:
            pass

        if atacante.ver_mana() < 20:
            raise ValueError("Error: Estás agotado")
        else:
            atacante.restar(20, "mana")
            defensor.restar(30, "vida")

            return f"¡{atacante.nombre} lanzó un poderoso hechizo a {defensor.nombre}!\n \nVitácora de la contienda:\n{atacante}\n{defensor}"
        
torneo_del_poder = Arena()
peleadores = [Personaje("Arthur"), Personaje("Mituri")]

print(torneo_del_poder.lanzar_hechizo(peleadores[0], peleadores[1]))
print(torneo_del_poder.lanzar_hechizo(peleadores[1], peleadores[0]))
print(torneo_del_poder.lanzar_hechizo(peleadores[0], peleadores[1]))
print(torneo_del_poder.lanzar_hechizo(peleadores[1], peleadores[0]))
print(torneo_del_poder.lanzar_hechizo(peleadores[0], peleadores[1]))