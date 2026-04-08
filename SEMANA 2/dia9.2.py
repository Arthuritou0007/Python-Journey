# Ejemplo en donde falla el "and"

edad = 17
tiene_dni = True

if edad >= 18 and tiene_dni == True:
    print("Puedes entrar")
else:
    print("No puedes entrar")

# edad >= 18 → Falso 
# tiene_dni == True → Verdadero 
# Como UNA falla, todo el if falla, entonces va al else.