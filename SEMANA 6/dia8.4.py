import flet as ft

def main(page):

    def cálculo(e):
        try:
            caja.label = "Precio base"
            precio = int(caja.value)
            porcentaje = (precio / 100) * 21
            total = precio + porcentaje
            texto.value = total
            
            if precio < 0:
                caja.label = "¡No se admiten números negativos!"
                texto.value = "0"
        except ValueError:
            caja.label = "¡Ingrese un dato válido!"

    caja = ft.TextField(label="Precio base", on_change=cálculo)
    texto = ft.Text("0")

    page.add(caja)
    page.add(texto)

ft.run(main)