capacidad = 0

while True:
    objeto = int(input("Ingrese el peso del objeto que quiere meter a la mochila: "))
    if objeto == 0:
        print(f"Mochila cerrada. Total de kgs almacenados: {capacidad}")
        break
    elif (capacidad + objeto) > 20:
        print(f"Capacidad máxima alcanzada. Kgs almacenados: {capacidad}")
        break
    elif (capacidad + objeto) == 20:
        capacidad = capacidad + objeto
        print(f"Capacidad máxima alcanzada. Kgs almacenados: {capacidad}")
        break
    else:
        capacidad = capacidad + objeto
        print(f"Objeto almacenado. Capacidad restante: {20 - capacidad}kgs")