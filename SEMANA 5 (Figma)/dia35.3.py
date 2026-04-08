import flet as ft

def main(page):
    texto1 = ft.Text("Soy azul", size=50, color=ft.Colors.BLUE, weight=ft.FontWeight.BOLD)
    texto2 = ft.Text("Soy rojo", size=50, color=ft.Colors.RED, weight=ft.FontWeight.BOLD)
    texto3 = ft.Text("Soy verde", size=50, color=ft.Colors.GREEN, weight=ft.FontWeight.BOLD)
    columna = ft.Column(controls=[texto1, texto2, texto3])

    page.add(columna)


ft.run(main)