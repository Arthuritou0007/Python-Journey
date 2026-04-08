numero = int(input("Ingrese un número entero: "))
total = 1

for vuelta in range(2, numero+1):
    anterior = total
    total = total * vuelta
    print(f"{anterior} X {vuelta} = {total}")