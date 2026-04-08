edad = int(input("Ingrese su edad: "))
viene_acompañado = int(input("Ingrese 1 si viene acompañado o 0 si viene solo: "))

if edad >= 18 or edad >= 13 and edad <= 17 and viene_acompañado == 1:
    print("Puede ingresar.")
else:
    print("No puede ingresar")