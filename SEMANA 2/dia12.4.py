numero_secreto = int(input("Ingrese un nùmero: "))

for i in range(1, 101, 1):
    if i == numero_secreto:
        print(f"¡Encontrè el nùmero! Lo enocntrè en el intento {i}")
        break
else:
    print("No encontrè el numero")