import flet as ft

def main(page):
    titulo = ft.Text("Manzanas", size=30, color=ft.Colors.RED, weight=ft.FontWeight.BOLD)
    precio = ft.Text("$1500", size=15, color=ft.Colors.GREEN)
    boton = ft.Button("COMPRAR")

    fila = ft.Row(controls=[precio, boton])
    columna = ft.Column(controls=[titulo, fila])

    page.add(columna)

ft.run(main)