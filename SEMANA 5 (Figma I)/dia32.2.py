import flet as ft

def main(page):
    titulo = ft.Text("¡App de la verdulería!", size=50, color=ft.Colors.PURPLE, weight=ft.FontWeight.BOLD)

    page.add(titulo)

ft.app(main)