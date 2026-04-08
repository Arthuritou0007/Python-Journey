import flet as ft

def main(page):

    def evento(e):
        texto.value = caja.value
        page.update()

    caja = ft.TextField(label="Ingrese su texto aquí", on_change=evento)
    texto = ft.Text(" ")

    page.add(caja)
    page.add(texto)

ft.run(main)