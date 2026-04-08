armas = ["Rota", "Buena", "Rota", "Legendaria", "Rota"]
contador = 0
oro = 1000

print(f"Armas: {armas[0]}, {armas[1]}, {armas[2]}, {armas[3]}, {armas[4]}")

for i in armas:
    if i == "Rota":
        contador = contador + 1

print(f"¡Se han econtrado {contador} armas rotas! ¿Quieres repararlas todas?")
print(f"Te saldrá un total de 100 de oro por cada arma dañada ({contador * 100}). Tu oro disponible es {oro}.")

respuesta = input("Ingresa tu respuesta (Si/No):")

if respuesta == "Si":
    oro = oro - (100 * contador)
    for arma in range(len(armas)):
        if armas[arma] == "Rota":
            armas[arma] = "Reparada"
    print(f"¡Has reparado todas tus armas! Ahora tu cantidad de oro es de {oro}")
    print(f"Armas: {armas[0]}, {armas[1]}, {armas[2]}, {armas[3]}, {armas[4]}")
else:
    print("No has reparado tus armas.")
    print(f"Armas: {armas[0]}, {armas[1]}, {armas[2]}, {armas[3]}, {armas[4]}")