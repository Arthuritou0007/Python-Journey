contraseña = "chipilipi123"

for i in range(3):
    contraseña_ingresada = input("Ingrese su contraseña: ")
    if contraseña_ingresada == contraseña:
        print("¡Contraseña correcta!")
        break
    else:
        print("Contraseña incorrecta.")
else:
    print("Límite de intentos alcanzado. Cuenta bloqueada")