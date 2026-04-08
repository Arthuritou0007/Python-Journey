capital = int(input("Ingrese su capital total:"))
gasto = int(input("Ingrese cuánto desea gastar:"))

if capital >= gasto:
    print("Compra realizada.")
    dinero_restante = capital - gasto
    print("Dinero restante: $" + str(dinero_restante))
else:
    print("No tienes dinero suficiente")
    dinero_faltante = gasto - capital
    print("Te faltan: $" + str(dinero_faltante), "para poder realizar esta compra.")