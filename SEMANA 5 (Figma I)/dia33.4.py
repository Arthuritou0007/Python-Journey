import flet as ft

def main(page):

    def suma(e):
        titulo.value = int(titulo.value)
        titulo.value = titulo.value + 1
        titulo.value = str(titulo.value)

        page.update()


    titulo = ft.Text("0", size=50, color=ft.Colors.BLUE, weight=ft.FontWeight.BOLD)
    boton = ft.Button("Sumar +1", on_click=suma)

    page.add(titulo)
    page.add(boton)

ft.run(main)