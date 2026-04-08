saldo = 1000
clave = "chipilipi123"
acceso = False

for i in range(1, 4):
    contraseña_ingresada = input("Ingrese su contraseña: ")
    if contraseña_ingresada == clave:
        print("Contraseña correcta, ¡bienvenido!")
        acceso = True
        break
    else:
        print(f"Contraseña incorrecta. Intento {i} de 3.")
else:
    print("Límite de intentos alcanzado. Tarjeta retenida.")

while acceso == True:
    print("Elija una de las opciones:")
    print("1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Depositar dinero")
    print("4. Salir")
    opcion = int(input("Ingrese aquí la opción que desee seleccionar: "))
    if opcion == 1:
        print(f"Su saldo es de ${saldo}")
        print("¿Desea volver al menú anterior?")
        print("1. Sí")
        print("2. No (Salir)")
        opcion = int(input("Ingrese aquí la opción que desee seleccionar: "))
        if opcion == 1:
            continue
        if opcion == 2:
            print("¡Hasta luego!")
            break
    if opcion == 2:
        acceso_retiro = False
        for i in range(1, 4):
            print("Para realizar un retiro, debe de ingresar su clave nuevamente.")
            contraseña_ingresada = input("Ingrese su contraseña: ")
            if contraseña_ingresada == clave:
                print("Contraseña correcta. Permiso concedido.")
                acceso_retiro = True
                break
            else:
                print(f"Contraseña incorrecta. Intento {i} de 3")
        else:
            print("Límites de intentos alcanzado. Tarjeta retenida.")
            acceso = False

        while acceso_retiro == True:
            retiro = int(input("Ingrese la cantidad de dinero que desea retirar: "))
            if retiro > saldo:
                print("No tienes dinero suficiente para retirar esa cantidad.")
                print("1. Volver al menú anterior.")
                print("2. Realizar otro retiro.")
                opcion = int(input("Ingrese aquí la opción que desee seleccionar: "))
                if opcion == 1:
                    break
                if opcion == 2:
                    continue
            else:
                saldo = saldo - retiro
                print(f"Has retirado ${retiro}, su saldo restante es de ${saldo}")
                print("1. Volver al menú anterior.")
                print("2. Realizar otro retiro.")
                opcion = int(input("Ingrese aquí la opción que desee seleccionar: "))
                if opcion == 1:
                    break
                if opcion == 2:
                    continue
    if opcion == 3:
        while True:
            ingreso = int(input("Ingrese la cantidad de dinero que quiere depositar: "))
            saldo = saldo + ingreso
            print(f"Has ingresado ${ingreso}, su nuevo saldo es de ${saldo}")
            print("1. Realizar otro depósito.")
            print("2. Volver al menú anterior.")
            opcion = int(input("Ingrese la aquí la opción que desee seleccionar: "))
            if opcion == 1:
                continue
            if opcion == 2:
                break
    if opcion == 4:
        print("¡Hasta luego!")
        break