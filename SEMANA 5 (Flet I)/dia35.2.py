import flet as ft

def main(page):
    boton1 = ft.Button("Inicio")
    boton2 = ft.Button("Perfil")
    boton3 = ft.Button("Ajustes")
    fila = ft.Row(controls=[boton1, boton2, boton3])

    page.add(fila)

ft.run(main)    