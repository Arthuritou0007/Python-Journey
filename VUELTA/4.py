energia = [15, 20, 10, 50]

def sumar_energia(lista_valores):
    contador = 0
    for i in lista_valores:
        contador = contador + i
        continue
    return contador

print(f"Energía: {sumar_energia(energia)}")