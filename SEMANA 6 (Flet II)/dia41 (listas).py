import flet as ft

def main(page):

    # 1. Creamos la mochila vacía desde el principio
    # El expand=True le permite estirarse hacia abajo
    mochila = ft.ListView(expand=True, spacing=10)

    def guardar_item(e):
        # 2. Leemos la palabra
        nuevo_item = caja_item.value
        
        # 3. Creamos un nuevo actor de texto
        texto_visual = ft.Text(f"🎒 {nuevo_item}", size=20)
        
        # 4. Magia: inyectamos el texto en la lista interna de la mochila
        mochila.controls.append(texto_visual)
        
        # 5. Vaciamos la caja para que el usuario no tenga que borrar a mano
        caja_item.value = ""
        
        # 6. Avisamos a la pantalla
        page.update()

    caja_item = ft.TextField(label="Nombre del ítem")
    boton = ft.Button("Guardar en mochila", on_click=guardar_item)

    page.add(caja_item, boton, mochila)

ft.run(main)