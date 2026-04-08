edad = int(input("Ingrese su edad:"))

if edad < 13:
    print("No puedes ingresar")
elif edad < 18:
    print("Puedes ingresar solo con un adulto")
else:
    print("Puedes ingresar libremente")