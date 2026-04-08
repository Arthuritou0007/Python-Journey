import flet as ft

def main(page):
    # 1. Tenés tu actor (puede ser un texto, un botón, o una caja organizadora)
    mi_texto = ft.Text("Hola", color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD)

    # 2. Lo metés adentro de la caja decorativa
    caja_linda = ft.Container(
        content=mi_texto, 
        bgcolor=ft.Colors.AMBER, # Color de fondo
        padding=20, # Relleno interno, para que el contenido no quede pegado a los bordes
        border_radius=10 # Redondea las esquinas de la caja
    )

    # 3. Subís la caja al escenario
    page.add(caja_linda)

ft.run(main)