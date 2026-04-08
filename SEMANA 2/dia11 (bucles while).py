# Los bucles "while", a diferencia de los "for", se utilzan para ejecutar un ciclo mientras una condición sea verdadera (true)

numero = 1

while numero < 5:
    print(f"El número vale: {numero}")
    numero = numero + 1  # 👈 ESTO ES VITAL.

# En este código le decimos a la computadora:
# Mientras (while) "numero" sea menor a 5, haz esto:
# Esto quiere decir que una vez la condición sea verdadera (es decir, que la variable "numero" valga menos que 5) se realizará la instrucción.
# Es importante, como en este caso, asegurarse que dentro del bucle se llegue a cumplir la condición.
# De lo contrario, se creará un bucle infinito y se deberá cerrar de forma forzada el programa.