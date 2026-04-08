maleta = ["Ropa", "Libro", "Bomba", "Laptop", "Agua"]

print(f"En la maleta hay {len(maleta)} objetos.")

for i in maleta:
    if i == "Bomba":
        print("¡PELIGRO DETECTADO! Deteniendo escaneo.")
        break
    elif i == "Agua":
        print("Líquido prohibido, tirando a la basura...")
        maleta.remove(i)
    else:
        print(f"Objeto {i} verificado.")