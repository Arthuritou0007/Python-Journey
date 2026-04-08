numero_a = int(input("Ingrese un número:"))
numero_b = int(input("Ingrese un segundo número:"))

if numero_a > numero_b:
    print(numero_a, "es mayo que", numero_b)
elif numero_b == numero_a:
    print("Son iguales")
else:
    print(numero_b, "es mayor que", numero_a)