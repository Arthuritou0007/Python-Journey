import flet as ft

def main(page):

    texto1 = ft.TextField(label="TEXTO EJEMPLO")
    boton1 = ft.Button("BOTON EJEMPLO")
    fila_ejemplo = ft.Row(controls=[texto1, boton1])

    texto2 = ft.TextField(label="TEXTO EJEMPLO 2")
    boton2 = ft.Button("BOTON EJEMPLO 2")
    columna_ejemplo = ft.Column(controls=[texto2, boton2])

    page.add(fila_ejemplo)
    page.add(ft.Text(" "))
    page.add(columna_ejemplo)

ft.run(main)