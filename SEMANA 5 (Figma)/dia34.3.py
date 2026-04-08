import flet as ft

def main(page):
    def evento(e):
        try:
            edad = int(caja.value)
            if edad >= 18:
                texto_final.value = "Puede ingresar"
                texto_final.color = ft.Colors.GREEN
                page.update()
            elif edad <= 0:
                texto_final.value = "¡Ingrese un dato válido!"
                texto_final.color = ft.Colors.PURPLE
                page.update()
            else:
                texto_final.value = "A casa"
                texto_final.color = ft.Colors.RED
                page.update()
        except ValueError:
            texto_final.value = "¡Ingrese un dato válido!"
            texto_final.color = ft.Colors.PURPLE
            page.update()

    caja = ft.TextField("Ingrese su edad")
    boton = ft.Button("Confirmar", on_click=(evento))
    texto_final = ft.Text(" ", size=50, weight=ft.FontWeight.BOLD)
    
    page.add(caja)
    page.add(boton)
    page.add(texto_final)

ft.run(main)