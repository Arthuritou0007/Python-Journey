numero_secreto = 4
numero_ingresado = int(input("Intente adivinar un número: "))

while numero_ingresado != numero_secreto:
    numero_ingresado = int(input("Número incorrecto. Inténtelo nuevamente: "))

print("¡Le atinaste al número!")