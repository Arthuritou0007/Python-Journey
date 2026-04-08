precio = int(input("Ingrese el precio del producto:"))
descuento = int(input("Ingrese el porcentaje de descuento que desea:"))
recargo = 0.1

porcentaje_descuento = descuento / 100
precio_descontado = precio - (porcentaje_descuento * precio)
precio_final = precio_descontado + (precio_descontado * recargo)

print("El precio de su producto es de $" + str(precio))
print("El descuento aplicado es del", str(descuento) + "%")
print("El precio de su producto aplicando el descuento es de $" + str(precio_descontado))
print("Aplicando el 10% de recargo por envìo, el precio final del producto es de $" + str(precio_final))