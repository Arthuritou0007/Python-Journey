import flet as ft

def main(page):
    def interaccion(e):
        mensaje_final.value = "Anotaste: " + caja_ingreso.value
        page.update()

    caja_ingreso = ft.TextField(label="Cantidad de kilos")
    boton = ft.Button("Confirmar", on_click=interaccion)
    mensaje_final = ft.Text(" ", size=50, weight=ft.FontWeight.BOLD)

    page.add(caja_ingreso)
    page.add(boton)
    page.add(mensaje_final)

ft.run(main)