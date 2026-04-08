import flet as ft

def main(page):
    boton1 = ft.Button("Inicio")
    boton2 = ft.Button("Perfil")
    boton3 = ft.Button("Ajustes")
    fila = ft.Row(controls=[boton1, boton2, boton3], alignment=ft.MainAxisAlignment.SPACE_EVENLY) # Reparte el espacio en blanco de forma equitativa entre todos los actores.
    fila2 = ft.Row(controls=[boton1, boton2, boton3], alignment=ft.MainAxisAlignment.SPACE_BETWEEN) # Empuja a los actores hacia los bordes, dejando el espacio vacío en el medio.
    fila3 = ft.Row(controls=[boton1, boton2, boton3], alignment=ft.MainAxisAlignment.CENTER) # Junta todo en el medio.

    page.add(fila)
    page.add(ft.Text(" "))
    page.add(ft.Text(" "))    
    page.add(fila2)
    page.add(ft.Text(" "))
    page.add(ft.Text(" "))        
    page.add(fila3)

ft.run(main)