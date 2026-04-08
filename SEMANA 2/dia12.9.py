contador = 0

for i in range(1, 5):
    numero = int(input("Ingrese un número: "))
    if numero < 0:
        print("No se pueden sumar números negativos.")
    else:
        anterior = contador
        contador = numero + contador
        print(f"Acaba de sumar {numero} a su cuenta de {anterior}, su cuenta es de {contador}")

print(f"El total de su suma es: {contador}")