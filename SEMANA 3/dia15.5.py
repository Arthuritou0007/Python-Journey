inventario = ["Espada", "Escudo", "Poción", "Antorcha"]
print(f"Inventario inicial: {inventario}")

print("¡Te has tomado una poción!")
inventario.remove("Poción")

print("¡Se te ha roto tu escudo!")
inventario.pop(1)

print("¡Has encontrado una gema!")
inventario.append("Gema")

print(f"Tu loot actual: {inventario}")