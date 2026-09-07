import os
from models import Pedido
from models import menu
from backend import cargar_datos
from backend import guardar_datos

def elegir_menu():
    contador = 1
    for i in menu:
        print(f"[{contador}] {i["Producto"]} ${i["Valor"]}")
        contador += 1

    eleccion = int(input("Ingresar: "))
    eleccion -= 1
    return menu[eleccion]

def chequeo_menu(lista, mesa):
    archivo_buscado = f"Mesa_{mesa}.json"
    if archivo_buscado in lista:
        while True:
            print("¡Cuidado! Ya habías ordenado en ésta mesa.\nSi continúas, sobreescribirás la orden anterior.\n¿Deseas continuar?\n[1] Sí\n[2] No")
            try:
                eleccion = int(input("Ingresar elección: "))
                if eleccion == 1:
                    return True
                if eleccion == 2:
                    return False
            except ValueError:
                print("¡Ingrese un dato válido!")
    return True
            

print("Abriendo menú interactivo de la hamburguesería...")
print("¡Bienvenido!")
while True:
    print("Ingrese la acción que desea realizar:")
    print("[1] Agregar un pedido")
    print("[2] Ver historial de pedidos")
    try:
        opcion = int(input("Ingresar opción: "))
        if opcion == 1:
            print("Rellene los datos:")
            comensal = input("Comensal: ")
            mesa = int(input("Mesa: "))
            lista_pedidos = os.listdir("POO EJERCICIO 2/PEDIDOS")
            puede_continuar = chequeo_menu(lista_pedidos, mesa)
            if puede_continuar == False:
                print("Cancelando pedido. Volviendo al menú principal...")
                continue
            pedido = Pedido(comensal, mesa)
            try: 
                producto = elegir_menu()
            except IndexError:
                print("¡Ingrese un dato válido!")
                continue
            pedido.agregar_producto(producto)
            while True:
                print("¿Desea agregar algo más?\n[1] Sí\n[2] No")
                try:
                    eleccion = int(input("Ingresar elección: "))
                    if eleccion == 1:
                        producto = elegir_menu()
                        pedido.agregar_producto(producto)
                    if eleccion == 2:
                        break
                except ValueError:
                    print("¡Ingrese un dato válido!")
            database = pedido.to_dict()
            guardar_datos(database)
        if opcion == 2:
            lista_pedidos = os.listdir("POO EJERCICIO 2/PEDIDOS")
            for i in lista_pedidos:
                numero_mesa = i.replace("Mesa_", "")
                numero_mesa = numero_mesa.replace(".json", "")
                print(f"Mesa N°{numero_mesa}")
            mesa = int(input("Ingrese la mesa que desea modificar o eliminar: "))
            datos_mesa = cargar_datos(mesa)
            print(f"Comensal: {datos_mesa['comensal']}")
            print(f"Mesa: {datos_mesa['mesa']}")
            print("---= PRODUCTOS =---")
            contador = 1
            for i in datos_mesa['productos']:
                print(f"[{contador}] {i['Producto']} ${i['Valor']}")
                contador += 1
            pedido = Pedido(datos_mesa['comensal'], datos_mesa['mesa'])
            pedido.productos = datos_mesa['productos']
            print("¿Qué desea hacer?")
            print("[1] Cobrar")
            print("[2] Modificar pedido")
            print("[3] Eliminar pedido")
            eleccion = int(input("Ingresar elección: "))
            if eleccion == 1:
                print(f"TOTAL A COBRAR: ${pedido.calcular_total()}")
                
    except ValueError:
        print("¡Igrese un número válido!")