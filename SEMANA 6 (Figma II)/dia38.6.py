import flet as ft

def main(page):

    def cálculo(e):
        try:
            ataque_jugador = int(ataque.value)
            defensa_enemigo = int(defensa.value)
            resultado = (ataque_jugador * 1.5) - defensa_enemigo
            if resultado <= 0:
                total.value = "0"
                page.update()
            else:
                total.value = str(resultado)
                page.update()
        except ValueError:
            total.value = "¡Ingresa un dato válido!"
            page.update()

    ataque = ft.TextField(label="Ataque del jugador")
    defensa = ft.TextField(label="Defensa del enemigo")
    boton = ft.Button("Calcular", on_click=cálculo)
    total = ft.Text(" ", color=ft.Colors.RED_ACCENT, weight=ft.FontWeight.BOLD, size=30)

    caja = ft.Container(
        content=total,
        bgcolor=ft.Colors.RED_900,
        padding=10,
        border_radius=10
    )

    page.add(ataque)
    page.add(defensa)
    page.add(boton)
    page.add(caja)

ft.run(main)