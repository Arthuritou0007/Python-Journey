class Cancion:
    def __init__(self, nombre_ingresado, duracion_ingresada):
        self.nombre = nombre_ingresado
        self._duracion = duracion_ingresada

    def ver_duracion(self):
        return self._duracion
    
    def ver_nombre(self):
        return self.nombre
    
class PlayList:
    def __init__(self):
        self.lista = []

    def agregar(self, cancion):
        self.lista.append(cancion)

    def sumar_segundos(self):
        contador = 0
        nombres = ""
        for i in self.lista:
            contador = contador + i.ver_duracion()
            nombres = nombres + f"Canción: {i.ver_nombre()}, Duración: {i.ver_duracion()}\n"
        
        return f"{nombres}\nDuración total de la Playlist: {contador} segundos"
    
canciones = [Cancion("Bohemian Rhapsody", 355), Cancion("Let It Be", 243)]

playlist_rock = PlayList()

playlist_rock.agregar(canciones[0])
playlist_rock.agregar(canciones[1])

print(f"{playlist_rock.sumar_segundos()}")