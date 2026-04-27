class Libro:
    def __init__(self, titulo_ingresado, autor_ingresado):
        self._disponible = True
        self.titulo = titulo_ingresado
        self.autor = autor_ingresado

    def disponible(self):
        if self._disponible == True:
            return True
        else:
            return False
        
    def __str__(self):
        return f"'{self.titulo}' escrito por {self.autor}" 
    
    def cambiar_estado(self):
        if self._disponible == True:
            self._disponible = False
        else:
            self._disponible = True
    
class Biblioteca:
    def __init__(self):
        self.catalogo = []
    
    def agregar_libro(self, libro):
        self.catalogo.append(libro)

    def prestar(self, libro):
        if libro.disponible() == True:
            libro.cambiar_estado()
            return f"Haz prestado el libro {libro}"
        else:
            raise ValueError("Error: Éste libro no está disponible")
        
tras_los_pasos = Biblioteca()
libros = [Libro("Hábitos Atómicos", "James Clear"), Libro("Sagas", "Okran")]

tras_los_pasos.agregar_libro(libros[0])
tras_los_pasos.agregar_libro(libros[1])

print(libros[0])
print(tras_los_pasos.prestar(libros[1]))
print(tras_los_pasos.prestar(libros[1]))