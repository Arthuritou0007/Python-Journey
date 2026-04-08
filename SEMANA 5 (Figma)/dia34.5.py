import flet as ft

def main(page):

    def acumular(e):
        try:
            contador = int(acumulador.value)
            numero = int(sumador.value)

            total = contador + numero
            acumulador.value = str(total)
            sumador.value = " "
            alerta.value = " "
            page.update()
        except ValueError:
            alerta.value = "¡Ingresa  un número válido!"
            page.update()

    acumulador = ft.Text("0", size=50)
    sumador = ft.TextField(label="Ingrese la cantidad que quiere sumar")
    boton = ft.Button("Sumar a la cuenta", on_click=(acumular))
    alerta = ft.Text(" ", color=ft.Colors.RED)

    page.add(acumulador)
    page.add(sumador)
    page.add(boton)
    page.add(alerta)

ft.run(main)