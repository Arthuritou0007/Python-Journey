contraseña_correcta = "chipilipi123"
contraseña_ingresada = input("Ingrese su contraseña:")

if contraseña_ingresada != contraseña_correcta:
    print("ACCESO DENEGADO.")
else:
    print("ACCESO PERMITIDO.")