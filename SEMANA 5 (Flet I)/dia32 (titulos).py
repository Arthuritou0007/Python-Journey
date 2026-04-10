import flet as ft

def main(page):
    titulo = ft.Text("Hola") # Creamos una variable y dentro de ella guardamos la función que nos hace tener un comentario en la app

    page.add(titulo) # Aquí hacemos que se agregue ese comentario a la app

ft.app(main)