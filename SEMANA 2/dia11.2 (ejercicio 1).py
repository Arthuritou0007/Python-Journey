contraseña = "chipilipi123"
clave_ingresada = input("Ingrese la contraseña: ")

while clave_ingresada != contraseña:
    print("Contraseña incorrecta.")
    clave_ingresada = input("Intente nuevamente: ")

print("¡Acceso concedido!")