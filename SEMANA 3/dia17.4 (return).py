# MALA PRÁCTICA (Solo imprime)
def sumar_malo(a, b):
    print(a + b)

resultado = sumar_malo(5, 5) # Imprime 10 en pantalla...
print(resultado) # ¡IMPRIME "None"! Porque la función no devolvió nada.

# BUENA PRÁCTICA (Retorna)
def sumar_bueno(a, b):
    return a + b # <--- ACÁ entrega el dato

mi_cuenta = sumar_bueno(5, 5) # No imprime nada, pero GUARA el 10 en la variable.
print(f"El resultado guardado es: {mi_cuenta}")