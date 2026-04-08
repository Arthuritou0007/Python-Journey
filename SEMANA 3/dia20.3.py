monstruos = [
    {"nombre": "Troll", "poder": 50},
    {"nombre": "Zodd", "poder": 9000},
    {"nombre": "Esqueleto", "poder": 30}
]

for i in monstruos:
    if i["poder"] > 100:
        print(f"¡Peligro extremo detectado: {i['nombre']}!")