# Los operadores lógicos se utilizan para combinar condiciones.

# En este caso se está utilizando el operador "and", el cual le dice a la computadora:
# "Si (if) esto y esto (and) se cumple, entonces sucede esto. Sino (else), pasará esto"
edad = 20
tiene_dni = True

if edad >= 18 and tiene_dni == True: # Aquí, se le dice a la computadora que si x es mayor de edad y tiene DNI, entonces ingresará.
    print("Puedes entrar") 
else:
    print("No puedes entrar")

# edad >= 18 → ¿Es verdadero? → Sí
# tiene_dni == True → ¿Es verdadero? → Sí
# Como AMBOS son verdaderos → se ejecuta el if.