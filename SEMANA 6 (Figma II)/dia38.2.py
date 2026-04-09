import flet as ft

def main(page):
    
    def descontar(e):
        valor = int(texto.value)
        porcentaje = (valor / 100) * 15
        total = valor - porcentaje
        texto.value = round(total, 2)

    texto = ft.Text("1000", size=50, color=ft.Colors.RED_900, weight=ft.FontWeight.BOLD)
    boton = ft.Button("Aplicar 15%", on_click=descontar)

    caja = ft.Container(
        content=texto,
        bgcolor=ft.Colors.RED,
        padding=10,
        border_radius=10,
    )

    page.add(caja)
    page.add(boton)

ft.run(main)