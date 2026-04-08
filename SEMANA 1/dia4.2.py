# A TENER EN CUENTA:
# La función "input" solo puede almacenar datos de STRING.
# Es decir, una operación como ésta siempre dará error:

numero = input("Ingrese un número:")
operacion = numero - 1

print(operacion)

# ¿Por qué dió error? Porque la consola no puede restarle un número a un string.