import flet as ft

def main(page):

    def izquierda(e):
        titulo_principal.value = "Fuiste por la izquierda"
        titulo_principal.color = ft.Colors.PURPLE

        page.update()

    def derecha(e):
        titulo_principal.value = "Fuiste por la derecha"
        titulo_principal.color = ft.Colors.BLUE

        page.update()

    titulo_principal = ft.Text("Elige una dirección", size=50, color=ft.Colors.GREEN, weight=ft.FontWeight.BOLD)
    boton_izquierda = ft.Button("Izquierda", on_click=izquierda)
    boton_derecha = ft.Button("Derecha", on_click=(derecha))

    page.add(titulo_principal)
    page.add(boton_izquierda)
    page.add(boton_derecha)

ft.run(main)