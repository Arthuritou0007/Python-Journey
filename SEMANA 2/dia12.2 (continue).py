# A diferencia del "break", el controlador "continue" se saltea la vuelta que le pedimos.
# Es decir, no va a cancelar todo el código, solo va a saltearse una vuelta en específico y seguir ejecutando el bucle.

for numero in range(1, 6):
    if numero == 3:
        continue  # <--- Ignora lo que sigue abajo y pasa al siguiente número
    
    print(numero)

# En este ejemplo, tenemos el bucle for y le decimos a la computadora (Cuando llegues a la vuelta 3, salteala)
# Entonces se salteará esa vuelta, pero va a continuar con los que siguen posterior a esa.