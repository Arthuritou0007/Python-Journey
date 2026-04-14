import flet as ft
import asyncio

# Simulación de base de datos (me gusta jugar con que ya estoy operando en backend jsjs):
nombre_de_usuario = "Arthuritou007"
contraseña = "chipilipi123"
inventario = ["🗡️ Daga oxidada", "❤️ Pósima"]
oro = 2000
tienda = [
    {"nombre": "⚔️ Espada Berserker", "precio": 1000},
    {"nombre": "❤️ Pósima", "precio": 50},
    {"nombre": "🍞 Pan", "precio": 100},
    {"nombre": "🗺️ Mapa Misterioso", "precio": 10}
]

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
        size=20,
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

def comprar(valor, item, control_oro, page):
    global oro # Avisamos que vamos a modificar el oro de afuera
    
    if oro >= valor:
        oro = oro - valor
        inventario.append(item)

        item_comprado = ft.Text(f"{item}", size=20, weight=ft.FontWeight.BOLD)
        mochila.controls.append(item_comprado)
        
        # Actualizamos el texto en pantalla
        control_oro.value = f"{str(oro)}" 
        page.update()
    else:
        print("¡No tienes suficiente oro!")



espacio_vacio = ft.Container(height=50)

# Pestaña del bosque:
def mostrar_juego(page):
    page.clean()

    def abrir_mochila(e):
        funcion_inventario(page)

    async def quedarse(e):
        await quedarse_en_el_lugar(page)

    async def acción_explorar(e):
        await explorar(page)

    texto1_bosque = crear_texto("Acabas de despertar... Tu cabeza da vueltas y no sabes en dónde estás.", ft.Colors.WHITE)
    texto2_bosque = crear_texto("Ves en frente de ti un camino entre los árboles que se extiende hacia la profundidad del bosque.", ft.Colors.WHITE)

    boton_bosque1 = ft.Button("Explorar", align=ft.Alignment.CENTER, width=250, height=60, on_click=acción_explorar)
    boton_bosque2 = ft.Button("Quedarse en el lugar", align=ft.Alignment.CENTER, width=250, height=60, on_click=quedarse)
    boton_bosque3 = ft.Button("Inventario", align=ft.Alignment.CENTER, width=250, height=60, on_click=abrir_mochila)

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
    cerrar_mochila = ft.Button("Cerrar mochila", align=ft.Alignment.CENTER, width=250, height=60, on_click=cerrar_inventario)
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

# Opción "Explorar"
async def explorar(page):
    page.clean()

    def volver_al_menú(e):
        page.clean()
        mostrar_juego(page)

    texto1_explorar = crear_subtitulo("Has caminado un largo sendero y encontraste una tienda", ft.Colors.WHITE)
    texto2_explorar = crear_subtitulo("Entras a la tienda y un hombre encapuchado se acerca a ti y por", ft.Colors.WHITE)
    texto3_explorar = crear_subtitulo("arte de magia hace aparecer 4 objetos encima del mostrador", ft.Colors.WHITE)
    texto4_explorar = crear_subtitulo('"Escoge sabiamente", te susurra entre risas', ft.Colors.WHITE)

    espada_berserker1 = crear_texto(f"{tienda[0]["nombre"]}", color=ft.Colors.BLUE_900)
    espada_berserker2 = ft.Button(f"COMPRAR (${tienda[0]["precio"]})", bgcolor=ft.Colors.BLUE_900, width=250, height=60, on_click=lambda e: comprar(tienda[0]["precio"], tienda[0]["nombre"], oro_disponible, page))
    espada_serberker3 = ft.Column(controls=[espada_berserker1, espada_berserker2], horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    pocima1 = crear_texto(f"{tienda[1]["nombre"]}", color=ft.Colors.BLUE_900)
    pocima2 = ft.Button(f"COMPRAR (${tienda[1]["precio"]})", bgcolor=ft.Colors.BLUE_900, width=250, height=60, on_click=lambda e: comprar(tienda[1]["precio"], tienda[1]["nombre"], oro_disponible, page))
    pocima3 = ft.Column(controls=[pocima1, pocima2], horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    primera_fila = ft.Row(controls=[espada_serberker3, pocima3], alignment=ft.MainAxisAlignment.SPACE_EVENLY)

    pan1 = crear_texto(f"{tienda[2]["nombre"]}", color=ft.Colors.BLUE_900)
    pan2 = ft.Button(f"COMPRAR (${tienda[2]["precio"]})", bgcolor=ft.Colors.BLUE_900, width=250, height=60, on_click=lambda e: comprar(tienda[2]["precio"], tienda[2]["nombre"], oro_disponible, page))
    pan3 = ft.Column(controls=[pan1, pan2], horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    mapa_misterioso1 = crear_texto(f"{tienda[3]["nombre"]}", color=ft.Colors.BLUE_900)
    mapa_misterioso2 = ft.Button(f"COMPRAR (${tienda[3]["precio"]})", bgcolor=ft.Colors.BLUE_900, width=250, height=60, on_click=lambda e: comprar(tienda[3]["precio"], tienda[3]["nombre"], oro_disponible, page))
    mapa_misterioso3 = ft.Column(controls=[mapa_misterioso1, mapa_misterioso2], horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    segunda_fila = ft.Row(controls=[pan3, mapa_misterioso3], alignment=ft.MainAxisAlignment.SPACE_EVENLY)

    cerrar_tienda = ft.Button(f"Volver al menú principal", bgcolor=ft.Colors.BLUE_900, width=250, height=60, on_click=volver_al_menú)

    oro_disponible = crear_texto(f"{str(oro)}", ft.Colors.YELLOW)
    oro_disponible2 = crear_texto(f"Oro: ", ft.Colors.WHITE)
    total_oro = ft.Row(controls=[oro_disponible2, oro_disponible])

    page.add(texto1_explorar, texto2_explorar, texto3_explorar, texto4_explorar, primera_fila, segunda_fila, cerrar_tienda, total_oro)


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
    boton_p1 = ft.Button("Iniciar sesión", align=ft.Alignment.CENTER, width=250, height=60, on_click=login)
    alerta_p1 = crear_subtitulo(" ", ft.Colors.BLUE_900)

    registro = ft.Row(controls=[ingresar_usuario_p1, ingresar_contraseña_p1], alignment=ft.MainAxisAlignment.CENTER)


    page.add(titulo_p1, espacio_vacio, subtitulo_p1, registro, espacio_vacio, boton_p1, alerta_p1)

ft.run(main)