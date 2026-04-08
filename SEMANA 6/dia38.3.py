import flet as ft

def main(page):

    def curarse(e):
        try:
            salud = int(vida.value)
            curacion = int(caja.value)
            total = salud + curacion

            if total > 100:    
                caja.value = "¡El límite de la salud de tu personaje es de 100!"
                page.update()
            elif curacion < 0:
                caja.value = "¡No se permiten números negativos!"
            else:
                vida.value = str(total)
                page.update()
        except ValueError:
            caja.value = "¡Ingrese un dato válido!"
            page.update()


    texto = ft.Text("Salud: ", size=50, weight=ft.FontWeight.BOLD, color=ft.Colors.RED_900)
    vida = ft.Text("50", size=50, weight=ft.FontWeight.BOLD, color=ft.Colors.RED_900)
    caja = ft.TextField(label="Puntos de curación")
    boton = ft.Button("Tomar poción", on_click=curarse)

    fila_salud = ft.Row(controls=[texto, vida], alignment=ft.MainAxisAlignment.SPACE_EVENLY)

    contenedor = ft.Container(
        content=fila_salud,
        bgcolor=ft.Colors.RED,
        width=275,
        padding=10,
        border_radius=10,
        alignment=ft.Alignment.CENTER
    )

    page.add(contenedor)
    page.add(caja)
    page.add(boton)

ft.run(main)