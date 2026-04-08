def calcular_descuento(cantidad, total):
    if cantidad >= 10:
        descuento = (total / 100) * 20
        return print(f"¡Ha conseguido un descuento! El monto total de su compra es de ${int(total - descuento)} (-${int(descuento)}!)")
    else:
        print(f"No hay ningún descuento. El total de su compra es de ${total}")

cantidad_comprada = int(input("Ingrese la cantidad de artículos que vaya a comprar: "))
precio = 100
total_compra = cantidad_comprada * precio

calcular_descuento(cantidad_comprada, total_compra)