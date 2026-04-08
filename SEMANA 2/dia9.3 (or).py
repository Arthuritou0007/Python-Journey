# A diferencia del "and", con el "or" con que una sola condición sea verdadera ya alcanza.

edad = 70

if edad < 12 or edad > 65:
    print("Entras gratis")
else:
    print("Pagas entrada normal")

# edad < 12 → Falso 
# edad > 65 → Verdadero 
# Como UNA es verdadera, el or se cumple → entra gratis.