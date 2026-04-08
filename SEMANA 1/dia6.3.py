precio = int(input("Ingrese el precio del producto:"))

if precio >= 500:
    descuento = precio - (precio * 0.20)
    print("¡Se aplicó un descuento del 20%! El precio final de su producto es de $" + str(descuento))
else:
    print("No se aplicó ningún descuento. El precio de su producto es de $" + str(precio))