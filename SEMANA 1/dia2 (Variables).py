Nombre = "Arthur"
Edad = 20
Cuadro = "Boca Juniors"
País = "Argentina"

print("Hola, soy", Nombre + ". Tengo", str(Edad) + ". Soy de", País, "y mi equipo es", Cuadro)

# El "," deja un espacio entre el string y la variable, el "+" no deja espacios.
# Aunque como la variable "Edad" está escrita como un número y no un string,
# hay que indicarle al programa que debe leerlo como una cadena de texto y no como un número.
# Para eso se utiliza el "str(variable)"