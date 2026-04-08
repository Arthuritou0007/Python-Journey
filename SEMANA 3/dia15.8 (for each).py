inventario = ["Espada", "Antorcha", "Arco"]

# Forma clásica: Un lío, tenés que usar i, len y corchetes
for i in range(len(inventario)):
    print(inventario[i])


# Forma pythonica: "Para cada objeto en el inventario..."
for objeto in inventario:
    print(f"Tenés: {objeto}")