def convertir_dolares_a_pesos(a):
    return a * 1200

dólares = int(input("Ingrese los dólares que quiere convertir a pesos: "))

conversión = convertir_dolares_a_pesos(dólares)

print(f"Sus ${dólares} dólares equivalen a ${conversión} pesos")