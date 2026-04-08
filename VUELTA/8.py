vida_zodd = 100

while vida_zodd > 0:
    poder_de_ataque = int(input("¿Con cuánto poder atacas?: "))

    vida_zodd = vida_zodd - poder_de_ataque

    if vida_zodd <= 0:
        print("Zodd ha sido derrotado!")
        break
    else:
        print(f"Zodd resiste. Le quedan {vida_zodd} puntos de vida")
        continue