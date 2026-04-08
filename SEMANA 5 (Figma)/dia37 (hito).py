import flet as ft

def main(page):
    
    def saludar(e):
        vacío.value = "¡Bienvenido a mi perfil, futuro Backend Engineer!"
        page.update()

    nombre = ft.Text("Arthur", size=50, color=ft.Colors.BLUE, weight=ft.FontWeight.BOLD)
    frase = ft.Text("Si estás pasando por un infierno, sigue caminando", color=ft.Colors.PURPLE, size=30, weight=ft.FontWeight.BOLD)
    vacío = ft.Text(". . .", size=30, weight=ft.FontWeight.BOLD, color=ft.Colors.RED)
    boton = ft.Button("Saludar", on_click=saludar)

    contenedor1 = ft.Container(
        content=nombre,
        bgcolor=ft.Colors.BLUE_900,
        padding=10,
        border_radius=10,
        margin=20
    )

    contenedor2 = ft.Container(
        content=frase,
        bgcolor=ft.Colors.PURPLE_900,
        padding=10,
        border_radius=10,
        margin=20
    )

    contenedor3 = ft.Container(
        content=vacío,
        bgcolor=ft.Colors.RED_900,
        padding=10,
        border_radius=10,
        margin=20
    )

    page.add(contenedor1)
    page.add(contenedor2)
    page.add(contenedor3)
    page.add(boton)

ft.run(main)