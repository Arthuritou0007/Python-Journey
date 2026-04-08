def calcular_daño(ataque, defensa):
    daño_real = ataque - defensa
    if daño_real < 0:
        return 0
    else:
        return daño_real
    
ataque_ingresado = int(input("Ingrese su ataque: "))
defensa_ingresada = int(input("Ingrese su defensa: "))

print(f"El daño causado es de {calcular_daño(ataque_ingresado, defensa_ingresada)}")