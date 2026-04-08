# Ejemplo donde falla el or

edad = 30

if edad < 12 or edad > 65:
    print("Entras gratis")
else:
    print("Pagas entrada normal")

# edad < 12 → Falso 
# edad > 65 → Falso 
# Como ninguna es verdadera → va al else.