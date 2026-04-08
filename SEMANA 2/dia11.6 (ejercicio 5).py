nota = 0

for i in range(1, 4):
    suma = int(input("Ingrese su nota: "))
    nota = suma + nota

promediado = nota / 3

print(f"Su promedio es de: {promediado}")