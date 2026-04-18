class Cuenta:
    def __init__(self, nombre_ingresado, contraseña_ingresada):
        self.nombre = nombre_ingresado
        self._contraseña = contraseña_ingresada

    def cambiar_password(self, nueva_clave):
        caracteres = len(nueva_clave)

        if caracteres < 8:
            raise ValueError("Error: La contraseña no puede contener menos de 8 caracteres.")
        else:
            self._contraseña = nueva_clave
            return f"Se ha modificado la contraseña para el usuario {self.nombre} Contraseña actualizada con éxito."


usuario1 = Cuenta("Arthur", "chipilipi123")

nueva_clave = input("Ingrese su nueva contraseña: ")

print(usuario1.cambiar_password(nueva_clave))