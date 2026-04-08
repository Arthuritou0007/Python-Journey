def crear_perfil(nombre, edad):
    return f"Personaje: {nombre} - Edad: {edad}"

nombre_ingresado = input("Ingrese su nombre: ")
edad_ingresada = int(input("Ingrese su edad: "))

print(crear_perfil(nombre_ingresado, edad_ingresada))