def contar_a(frase):
    contador = 0
    for i in frase:
        if i == "a" or i == "A":
            contador = contador + 1
    return contador

frase_dada = input("Ingrese su frase: ")

print(f"Su frase tiene {contar_a(frase_dada)} letras A")



