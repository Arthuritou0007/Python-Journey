edad = int(input("Ingrese su edad:"))
tiene_dni = int(input("Ingrese 1 si tiene DNI o 0 si no tiene:"))

if edad >= 18 and tiene_dni == 1:
    print("Puedes ingresar.")
else:
    print("No puedes ingresar.")