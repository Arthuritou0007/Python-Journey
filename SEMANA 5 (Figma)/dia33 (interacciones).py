import flet as ft

def main(page):

    def cambiar_mensaje(e):
        titulo.value = "¡Comenzamos!"
        page.update()


    titulo = ft.Text("¡App de la Verdulería!", size=50, color=ft.Colors.PURPLE, weight=ft.FontWeight.BOLD)
    boton = ft.Button("Comenzar", color=ft.Colors.GREEN, on_click=(cambiar_mensaje))

    page.add(titulo)
    page.add(boton)

ft.run(main)