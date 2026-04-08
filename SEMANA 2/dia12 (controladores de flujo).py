# Primer controlador: break.
# El controlador "break" se utiliza para cancelar todo el bucle y pasar a las líneas de código escritas por debajo.

for numero in range(1, 11):
    if numero == 5:
        print("¡Cortamos aquí!")
        break  # <--- Salta fuera del bucle inmediatamente
    
    print(numero)

# En este ejemplo, le decimos a la computadora "Cuando llegues a la vuelta 5, cortá todo el bucle"
# Entonces, a pesar de que debía hacer 10 vueltas, solo hizo 4 porque al llegar a la quinta abortó la orden.