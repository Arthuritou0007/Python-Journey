import flet as ft

def main(page):

    def cambiar_mensaje(e):
        titulo.value = "Encendido"
        titulo.color = ft.Colors.GREEN
        page.update()

    titulo = ft.Text("Apagado.", size=50, color=ft.Colors.RED, weight=ft.FontWeight.BOLD)
    boton = ft.Button("Tocar", color=ft.Colors.BLUE, on_click=(cambiar_mensaje))

    page.add(titulo)
    page.add(boton)

ft.run(main)