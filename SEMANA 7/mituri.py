espada_berserker = [
    {"daño": 20},
    {"encantamiento": "Filo II"}
]

print(f"Posees la espada Berserk con un daño de {espada_berserker[0]["daño"]}")

if espada_berserker[1]["encantamiento"] == "Filo II":
    porcentaje = espada_berserker[0]["daño"] / 100
    espada_berserker[0]["daño"] = espada_berserker[0]["daño"] + (porcentaje * 20)
    print(f"Gracias a tu encantamiento ({espada_berserker[1]["encantamiento"]}), tu espada ahora posee un daño de {espada_berserker[0]["daño"]}")
else:
    print("No posees ningún encantamiento")