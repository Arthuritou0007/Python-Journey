import flet as ft
import asyncio

# Simulación de base de datos (me gusta jugar con que ya estoy operando en backend jsjs):
nombre_de_usuario = "Arthuritou007"
contraseña = "chipilipi123"
inventario = ["🗡️ Daga oxidada", "❤️ Pósima"]

# Inventario: 
items_visuales = []

for nombre in inventario:
    items_visuales.append(ft.Text(f"{nombre}", size=20, weight=ft.FontWeight.BOLD))

mochila = ft.Column(spacing=10, controls=items_visuales)


# Funciones para falicitar los textos:
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


# Pestaña del bosque:
def mostrar_juego(page):
    page.clean()

    def abrir_mochila(e):
        funcion_inventario(page)

    async def quedarse(e):
        await quedarse_en_el_lugar(page)

    texto1_bosque = crear_texto("Acabas de despertar... Tu cabeza da vueltas y no sabes en dónde estás.", ft.Colors.WHITE)
    texto2_bosque = crear_texto("Ves en frente de ti un camino entre los árboles que se extiende hacia la profundidad del bosque.", ft.Colors.WHITE)

    boton_bosque1 = ft.ElevatedButton("Explorar", align=ft.Alignment.CENTER, width=250, height=60)
    boton_bosque2 = ft.ElevatedButton("Quedarse en el lugar", align=ft.Alignment.CENTER, width=250, height=60, on_click=quedarse)
    boton_bosque3 = ft.ElevatedButton("Inventario", align=ft.Alignment.CENTER, width=250, height=60, on_click=abrir_mochila)

    fila_bosque = ft.Row(controls=[boton_bosque1, boton_bosque2], alignment=ft.MainAxisAlignment.SPACE_EVENLY)

    page.add(texto1_bosque, texto2_bosque, fila_bosque, boton_bosque3)
    page.update()

# Opción "Inventario"
def funcion_inventario(page):
    page.clean()

    def cerrar_inventario(e):
        page.clean()
        mostrar_juego(page)

    texto = crear_titulo("Inventario:", ft.Colors.BROWN)
    cerrar_mochila = ft.ElevatedButton("Cerrar mochila", align=ft.Alignment.CENTER, width=250, height=60, on_click=cerrar_inventario)
    contenedor_mochila = ft.Container(
        content=mochila,
        align=ft.Alignment.CENTER,
        bgcolor=ft.Colors.BROWN_900,
        padding=20,
        border_radius=10
        )

    page.add(texto, contenedor_mochila, cerrar_mochila)

# Opción "Quedarse en el lugar"
async def quedarse_en_el_lugar(page):
    page.clean()

    texto1_quedarse = crear_titulo("No te has movido ni un pelo...", ft.Colors.WHITE)
    page.add(texto1_quedarse)

    await asyncio.sleep(3)

    mostrar_juego(page)


def main(page):

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    async def login(e):
        
        if ingresar_contraseña_p1.value == contraseña and ingresar_usuario_p1.value == nombre_de_usuario:
            page.clean()
            page.add(crear_titulo(f"¡Bienvenido, {nombre_de_usuario}!", ft.Colors.WHITE))
            page.add(crear_subtitulo("Redirigiendo...", ft.Colors.WHITE))
            page.update()

            await asyncio.sleep(3)

            mostrar_juego(page)

        else:
            alerta_p1.value = "Los datos ingresados son incorrectos. Intente nuevamente"
            page.update()

    espacio_vacio = ft.Container(height=50)

    titulo_p1 = crear_titulo("--=== ¡Bienvenido a LK Dungeon Quest! ===--", ft.Colors.BLUE_900)
    subtitulo_p1 = crear_subtitulo("Para continuar, debe iniciar sesión", ft.Colors.BLUE_900)
    ingresar_usuario_p1 = crear_textfield("Ingrese aquí su nombre de usuario", ft.Colors.BLUE, ft.Colors.BLUE_900)
    ingresar_contraseña_p1 = crear_textfield("Ingrese aquí su contraseña", ft.Colors.BLUE, ft.Colors.BLUE_900)
    boton_p1 = ft.ElevatedButton("Iniciar sesión", align=ft.Alignment.CENTER, width=250, height=60, on_click=login)
    alerta_p1 = crear_subtitulo(" ", ft.Colors.BLUE_900)

    registro = ft.Row(controls=[ingresar_usuario_p1, ingresar_contraseña_p1], alignment=ft.MainAxisAlignment.CENTER)


    page.add(titulo_p1, espacio_vacio, subtitulo_p1, registro, espacio_vacio, boton_p1, alerta_p1)

ft.run(main)