import flet as ft

def main(page):

    def evento(e):
        texto.value = caja.value.upper()
        page.update()

    caja = ft.TextField(" ")
    boton = ft.Button("Gritar", on_click=evento)
    texto = ft.Text("  ", size=50)

    page.add(caja)
    page.add(boton)
    page.add(texto)

ft.run(main)