import flet as ft

def main(page):
    manzana = ft.Text("Manzana", size=30, color=ft.Colors.RED, weight=ft.FontWeight.BOLD)
    banana = ft.Text("Banana", size=30, color=ft.Colors.YELLOW, weight=ft.FontWeight.BOLD)

    caja1 = ft.Container(
        content=manzana,
        margin=20,
        bgcolor=ft.Colors.GREEN,
        border_radius=10,
        padding=10,
        width=150,
        height=75,
        alignment=ft.Alignment.CENTER
    )

    caja2 = ft.Container(
        content=banana,
        margin=20,
        bgcolor=ft.Colors.PURPLE,
        border_radius=10,
        padding=10,
        width=150,
        height=75,
        alignment=ft.Alignment.CENTER
    )

    fila = ft.Row(controls=[caja1, caja2], alignment=ft.MainAxisAlignment.CENTER)

    page.add(fila)

ft.run(main)