import flet as ft

def main(page):

    def operación(e):
        try:
            precio = int(caja_precio.value)
            descuento = int(caja_descuento.value)
            precio_total = precio - descuento
            total.value = str(precio_total)
            page.update()
        except ValueError:
            total.value = "¡Ingrese un dato válido!"
            total.color = ft.Colors.RED
            page.update()


    
    caja_precio = ft.TextField("Ingrese el precio del producto")
    caja_descuento = ft.TextField("Ingrese su descuento")
    boton = ft.Button("Calcular", on_click=operación)
    total = ft.Text(" ", size=50)

    page.add(caja_precio)
    page.add(caja_descuento)
    page.add(boton)
    page.add(total)

ft.run(main)