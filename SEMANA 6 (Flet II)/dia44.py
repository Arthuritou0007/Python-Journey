import flet as ft

def crear_titulo(texto, color):
    return ft.Text(
        f"{texto}",
        size=50,
        color=color,
        weight=ft.FontWeight.BOLD,
        align=ft.Alignment.CENTER
    )

def crear_subtitulo(texto, color):
    return ft.Text(
        f"{texto}",
        size=30,
        color=color,
        weight=ft.FontWeight.BOLD,
        align=ft.Alignment.CENTER
    )

def crear_textfield(label, color, color2):
    return ft.TextField(
        label=label,
        color=color,
        bgcolor=color2
    )

# Simulación de base de datos (me gusta jugar con que ya estoy operando en backend jsjs):

nombre_de_usuario = "Arthuritou007"
contraseña = "chipilipi123"

def main(page):

    espacio_vacio = ft.Container(height=50)

    titulo_p1 = crear_titulo("--=== ¡Bienvenido a LK Dungeon Quest! ===--", ft.Colors.BLUE_900)
    subtitulo_p1 = crear_subtitulo("Para continuar, debe iniciar sesión", ft.Colors.BLUE_900)
    ingresar_usuario = crear_textfield("Ingrese aquí su nombre de usuario", ft.Colors.BLUE, ft.Colors.BLUE_900)
    ingresar_contraseña = crear_textfield("Ingrese aquí su contraseña", ft.Colors.BLUE, ft.Colors.BLUE_900)
    boton = ft.ElevatedButton("Iniciar sesión", align=ft.Alignment.CENTER, width=250, height=60)

    registro = ft.Row(controls=[ingresar_usuario, ingresar_contraseña], alignment=ft.MainAxisAlignment.SPACE_EVENLY)


    page.add(titulo_p1, espacio_vacio, subtitulo_p1, registro, espacio_vacio, boton)

ft.run(main)