frase = input("Ingrese una frase: ")
letra = input("Ingrese qué letra quiere identificar: ")
contador = 0

for i in frase:
    if i == letra:
        contador = contador + 1

print(f"Su frase tiene {contador} letras '{letra}'")