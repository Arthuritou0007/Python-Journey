import flet as ft

def main(page):
        
    def atacar(e):
        vida = int(texto.value)
        total = vida - 15
        texto.value = str(total)


        if total <= 0:
          texto.value = "¡El enemigo ha sido derrotado!"
          page.remove(boton)

        page.update()

    texto = ft.Text("100", size=50, color=ft.Colors.RED)
    boton = ft.Button("Atacar", on_click=atacar)



    page.add(texto)
    page.add(boton)


        

ft.run(main)