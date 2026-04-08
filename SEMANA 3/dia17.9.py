def generar_email(nombre, apellido, año):
    for i in nombre:
        primera_letra = i
        break
    return f"{primera_letra}{apellido}{año}@gmail.com"

nombre_dado = input("Ingrese su nombre: ")
apellido_dado = input("Ingrese su apellido: ")
año_dado = int(input("Ingrese su año de nacimiento: "))

print(f"Su correo generado es: {generar_email(nombre_dado, apellido_dado, año_dado)}")