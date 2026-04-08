precio = int(input("Ingrese el precio de su producto:"))
descuento = float(input("Ingrese el descuento deseado en decimales:"))
recargo = 0.10

precio_descontado = precio - (precio * descuento)
precio_final = precio_descontado + (precio_descontado * recargo)

print("El precio de su producto es de:", precio)
print("Aplicando su descuento de", descuento, "su producto queda con un valor total de:", precio_descontado)
print("Aplicando el recargo por envío del", recargo, ", su producto queda con un coste final de:", precio_final)