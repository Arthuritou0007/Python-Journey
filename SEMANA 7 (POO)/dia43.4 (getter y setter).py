class Producto:
    def __init__(self, nombre_ingresado, kilos_iniciales):
        self.nombre = nombre_ingresado
        # Le ponemos el candado a los kilos usando el guión bajo
        self._stock = kilos_iniciales

    # 👁️ EL GETTER (La ventanilla para mirar)
    def ver_stock(self):
        return self._stock

    # 🛡️ EL SETTER (El guardia de seguridad que armaste vos)
    def actualizar_stock(self, nuevos_kilos):
        if nuevos_kilos < 0:
            # Si rompen la regla, el guardia grita el error y frena todo
            raise ValueError("Error: El stock no puede ser un número negativo.")
        else:
            # Si todo está bien, actualiza el dato guardado bajo llave
            self._stock = nuevos_kilos
            return f"Stock actualizado exitosamente a {self._stock} kilos."
        
papas = Producto("Papas negras", 17)

nuevos_kilos = int(input("Ingrese los kg nuevos de las papas:"))

print(papas.actualizar_stock(nuevos_kilos))