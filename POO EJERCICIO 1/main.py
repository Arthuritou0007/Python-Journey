from models import Mascota
from backend import guardar_datos
from backend import obtener_lista_pacientes
from backend import cargar_datos

print("¡Hola! Bienvenido al menú interactivo")
while True:
    print("Escribe en la caja de texto la opción que desees:")
    print("[1] Ingresar a la base de datos")
    print("[2] Salir del menú")
    try:
        opcion = int(input("Ingresar opción:"))
        if opcion == 1:
            print("Abriendo base de datos...")
            print("Ha entrado a la base de datos.")
            while True:
                print("[1] Registrar una nueva mascota")
                print("[2] Ver mascotas registradas")
                try:
                    opcion = int(input("Ingresar opción:"))
                    if opcion == 1:
                        nombre = input("Ingrese el nombre de la mascota:")
                        animal = input("Ingrese qué animal es:")
                        dueño = input("Ingrese el nombre del dueño:")
                        motivo = input("Ingrese el motivo de la consulta:")

                        mascota = Mascota(nombre, animal, dueño, motivo)
                        guardar_datos(mascota.to_dict())

                        print("¡La mascota ha sido registrada con éxito!")
                        print("¿Desea registrar otra mascota?")
                        print("[1] Sí")
                        print("[2] No (Salir)")
                        try:
                            opcion = int(input("Ingresar opción:"))

                            if opcion == 1:
                                continue
                            if opcion == 2:
                                break
                            else:
                                print("¡Ingrese un dato válido!")
                        except ValueError:
                            print("¡Ingrese un dato válido!")
                    if opcion == 2:
                        print("Mostrando base de datos...")
                        contador = 1
                        lista_archivos = obtener_lista_pacientes()
                        for nombre in lista_archivos:
                            print(f"[{contador}] {nombre}")
                            contador += 1
                        print("¿A qué paciente desea acceder?")
                        try:
                            opcion = int(input("Ingresar opción (Numérica):"))
                            opcion_final = opcion - 1
                            datos = cargar_datos(lista_archivos[opcion_final])
                            print(f"Nombre: {datos['nombre']}")
                            print(f"Animal: {datos['animal']}")
                            print(f"Dueño: {datos['dueño']}")
                            print(f"Motivo de la consulta: {datos['motivo']}")
                        except ValueError:
                            print("¡Ingrese un dato válido!")
                except ValueError:
                    print("¡Ingrese un dato válido!")
        if opcion == 2:
            print("¡Hasta luego!")
            break
        else:
            print("¡Ingrese un dato válido!")
    except ValueError:
        print("¡Ingrese un dato válido!")