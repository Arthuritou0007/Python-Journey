import flet as ft
import asyncio

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

def crear_texto(texto, color):
    return ft.Text(
        f"{texto}",
        size=15,
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


# Segunda pestaña:
def mostrar_juego(page):
    page.clean()
    texto1_p2 = crear_texto("Acabas de despertar... Tu cabeza da vueltas y no sabes en dónde estás.", ft.Colors.WHITE)
    texto2_p2 = crear_texto("Ves en frente de ti un camino entre los árboles que se extiende hacia la profundidad del bosque", ft.Colors.WHITE)
    texto3_p2 = crear_texto("¿", ft.Colors.WHITE)
    page.add(texto1_p2)
    page.add(texto2_p2)
    page.add(texto3_p2)
    page.update()

# Simulación de base de datos (me gusta jugar con que ya estoy operando en backend jsjs):

nombre_de_usuario = "Arthuritou007"
contraseña = "chipilipi123"
inventario = ["🗡️ Daga oxidada", "❤️ Pósima"]

def main(page):

    async def login(e):
        
        if ingresar_contraseña_p1.value == contraseña and ingresar_usuario_p1.value == nombre_de_usuario:
            page.clean()
            page.add(crear_titulo(f"¡Bienvenido {nombre_de_usuario}!", ft.Colors.WHITE))
            page.add(crear_subtitulo("Redirigiendo...", ft.Colors.WHITE))
            page.update()

            await asyncio.sleep(3)

            mostrar_juego(page)

        else:
            alerta_p1.value = "Los datos ingresados son incorrectos. Intente nuevamente"
            page.update()

    items_visuales = []

    for nombre in inventario:
        items_visuales.append(ft.Text(f"{nombre}", size=20))

    mochila = ft.ListView(expand=True, spacing=10, controls=items_visuales)

    espacio_vacio = ft.Container(height=50)

    titulo_p1 = crear_titulo("--=== ¡Bienvenido a LK Dungeon Quest! ===--", ft.Colors.BLUE_900)
    subtitulo_p1 = crear_subtitulo("Para continuar, debe iniciar sesión", ft.Colors.BLUE_900)
    ingresar_usuario_p1 = crear_textfield("Ingrese aquí su nombre de usuario", ft.Colors.BLUE, ft.Colors.BLUE_900)
    ingresar_contraseña_p1 = crear_textfield("Ingrese aquí su contraseña", ft.Colors.BLUE, ft.Colors.BLUE_900)
    boton_p1 = ft.ElevatedButton("Iniciar sesión", align=ft.Alignment.CENTER, width=250, height=60, on_click=login)
    alerta_p1 = crear_subtitulo(" ", ft.Colors.BLUE_900)

    registro = ft.Row(controls=[ingresar_usuario_p1, ingresar_contraseña_p1], alignment=ft.MainAxisAlignment.SPACE_EVENLY)


    page.add(titulo_p1, espacio_vacio, subtitulo_p1, registro, espacio_vacio, boton_p1, alerta_p1)

ft.run(main)