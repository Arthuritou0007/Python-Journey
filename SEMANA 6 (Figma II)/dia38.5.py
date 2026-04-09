import flet as ft

def main(page):
    
    inventario = []
    oro = 500
    tienda = [
        {"nombre": "Espada", "precio": 300},
        {"nombre": "Escudo", "precio": 250}
    ]

    def comprar_espada(e):
        nonlocal oro
        nonlocal inventario
        if oro >= tienda[0]["precio"]:
            boton_espada.text = f"Comprar {tienda[0]['nombre']} (${str(tienda[0]['precio'])})"
            oro = oro - tienda[0]["precio"]
            inventario.append(tienda[0]["nombre"])
            texto_oro.value = f"Oro: {str(oro)}"
            texto_inventario.value = f"Inventario: {inventario}"
            page.update()
        else:
            boton_espada.text = "¡No tienes dinero suficiente para realizar esa compra!"
            page.update()

    def comprar_escudo(e):
        nonlocal oro
        nonlocal inventario
        if oro >= tienda[1]["precio"]:
            boton_escudo.text = f"Comprar {tienda[1]['nombre']} (${str(tienda[1]['precio'])})"
            oro = oro - tienda[1]["precio"]
            inventario.append(tienda[1]["nombre"])
            texto_oro.value = f"Oro: {str(oro)}"
            texto_inventario.value = f"Inventario: {inventario}"
            page.update()
        else:
            boton_escudo.text = "¡No tienes dinero suficiente para realizar esa compra!"
            page.update()

    texto_oro = ft.Text(f"Oro: {str(oro)}", size=50, weight=ft.FontWeight.BOLD, color=ft.Colors.YELLOW_900)
    texto_inventario = ft.Text(f"Inventario: {inventario}", size=30, weight=ft.FontWeight.BOLD)
    boton_espada = ft.Button(f"Comprar {tienda[0]['nombre']} (${str(tienda[0]['precio'])})", on_click=comprar_espada)
    boton_escudo = ft.Button(f"Comprar {tienda[1]['nombre']} (${str(tienda[1]['precio'])})", on_click=comprar_escudo)





    page.add(texto_oro)
    page.add(texto_inventario)
    page.add(boton_espada)
    page.add(boton_escudo)

ft.run(main)