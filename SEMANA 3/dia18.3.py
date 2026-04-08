saldo = 10000

def comprar_item(dinero_disponible, precio_item):
    if dinero_disponible >= precio_item:
        dinero_disponible = dinero_disponible - precio_item
        print(f"Compra exitosa, saldo restante: {dinero_disponible}")
        return dinero_disponible
    else:
        print("Dinero insuficiente")
        return dinero_disponible
    
zapato = 1000
lapiz = 500
media = 2000

carrito = [zapato, lapiz, media]

for i in carrito:
    saldo = comprar_item(saldo, i)

