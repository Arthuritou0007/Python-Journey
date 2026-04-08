capital = int(input("Ingrese su dinero: "))
precio_producto = 4000
stock = False # Supongamos que no

if capital > precio_producto and stock == True:
    dinero_restante = capital - precio_producto
    print("Compra realizada")
    print("Dinero restante $" + str(dinero_restante))
elif capital > precio_producto and stock == False:
    print("No hay stock suficiente para realizar la compra")
else:
    dinero_faltante = precio_producto - capital
    print("No puedes realizar la compra")
    print("Te faltan $" + str(dinero_faltante) + " para realizar esta compra")


# La verdad, me parecía un sin sentido que una condición tenga que ser que el precio sea mayor a 0 XD.
# Entonces, pensé en otra condición y se me ocurrió lo del stock