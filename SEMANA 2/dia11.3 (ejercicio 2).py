objetivo = 1000
ahorrado = 0

while ahorrado < objetivo:
    suma = int(input("Ingrese cuánto quiere poner en la alcancía: "))
    ahorrado = ahorrado + suma
    faltante = objetivo - ahorrado
    if ahorrado < objetivo:
        print(f"Lleva ${ahorrado} ahorrados")
        print(f"Le faltan ${faltante} para llegar a su objetivo de ${objetivo}")

print("Objetivo alcanzado")
print(f"Su ahorro total es de {ahorrado}")