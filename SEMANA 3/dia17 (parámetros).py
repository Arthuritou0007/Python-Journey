# Ponemos una variable entre los paréntesis del def. Esa variable va a actuar como un buzón para recibir datos.
# Definición: Le digo que espere un "nombre"
def saludar(nombre):
    print(f"Hola {nombre}, bienvenido al sistema.")

# Llamada: Le paso el dato real
saludar("Juan")  # Imprime: Hola Juan...
saludar("Ana")   # Imprime: Hola Ana...

# ¿Qué pasó ahí? Cuando escribís saludar("Juan"), la palabra "Juan" viaja y se guarda automáticamente en la variable nombre dentro de la función.