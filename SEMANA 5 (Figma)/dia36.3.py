import flet as ft

def main(page):
    texto1 = ft.Text("Manzana", color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD)
    texto2 = ft.Text("$1500", color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD)
    boton = ft.Button("COMPRAR")
    fila = ft.Row(controls=[texto1, texto2, boton], alignment=ft.MainAxisAlignment.CENTER)

    caja = ft.Container(
        content=fila,
        bgcolor=ft.Colors.WHITE,
        padding=20,
        border_radius=10,
        margin=10
    )

    page.add(caja)

ft.run(main)