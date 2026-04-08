contraseña = "chipilipi123"

while True:
    contraseña_ingresada = input("Ingrese su contraseña: ")
    if contraseña_ingresada == contraseña:
        print("Contraseña correcta!")
        break
    else:
        print("Contraseña incorrecta.")
        continue