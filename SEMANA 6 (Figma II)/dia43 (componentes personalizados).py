import flet as ft

def crear_texto(texto, color):
    return ft.Text(
        f"{texto}",
        weight=ft.FontWeight.BOLD,
        size=50,
        color=color
    )

def main(page):

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
        

    bienvenida = crear_texto("Portal de Aventureros", ft.Colors.LIGHT_GREEN_900)
    ingresar_usuario = ft.TextField(label="Ingrese su nombre")
    boton = ft.Button("Ingresar", on_click=ir_a_refugio)

    bienvenida_refugio = crear_texto(" ", ft.Colors.BLUE)
    boton_refugio = ft.Button("Cerrar sesiòn", on_click=volver_a_menu)

    page.add(bienvenida)
    page.add(ingresar_usuario)
    page.add(boton)

ft.run(main)