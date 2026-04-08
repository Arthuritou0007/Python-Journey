def es_par(numero):
    resultado = numero % 2
    if resultado == 0:
        return True
    else:
        return False
    
numero_dado = int(input("Ingrese un número: "))

if es_par(numero_dado):
    print("Es par.")
else:
    print("Es impar.")