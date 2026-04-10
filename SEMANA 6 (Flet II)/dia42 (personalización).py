import flet as ft

def main(page):
    page.theme_mode = ft.ThemeMode.DARK

    def ir_a_refugio(e):
        page.clean()
        page.add(bienvenida_refugio)
        page.add(boton_refugio)
        bienvenida_refugio.value = f"¡Bienvenido al refugio, {ingresar_usuario.value}!"
        page.update()

    def volver_a_menu(e):
        page.clean()
        page.add(bienvenida)
        page.add(ingresar_usuario)
        page.add(boton)
        page.update()
        

    bienvenida = ft.Text("Portal de Aventureros", size=50, weight=ft.FontWeight.BOLD, color=ft.Colors.LIGHT_GREEN_900)
    ingresar_usuario = ft.TextField(label="Ingrese su nombre", color=ft.Colors.GREEN, bgcolor=ft.Colors.LIGHT_GREEN_900)
    boton = ft.ElevatedButton("Ingresar", on_click=ir_a_refugio, bgcolor=ft.Colors.LIGHT_GREEN_900, color=ft.Colors.GREEN)

    bienvenida_refugio = ft.Text(f" ", size=50, color=ft.Colors.BLUE, weight=ft.FontWeight.BOLD)
    boton_refugio = ft.ElevatedButton("Cerrar sesiòn", on_click=volver_a_menu, bgcolor=ft.Colors.BLUE, color=ft.Colors.BLUE_900)

    page.add(bienvenida)
    page.add(ingresar_usuario)
    page.add(boton)

ft.run(main)