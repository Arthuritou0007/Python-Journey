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
    while True:
        for i in lista:
            if f"Mesa_{mesa}" == i:
                print("¡Cuidado! Ya habías ordenado en ésta mesa.\nSi continúas, sobreescribirás la orden.\n¿Deseas continuar?\n[1] Sí\n[2] No")
                try:
                    eleccion = int(input("Ingresar elección:"))
                    if eleccion == 1:
                        return True
                    if eleccion == 2:
                        return False
                except ValueError:
                    print("¡Ingrese un dato válido!")
            

print("Abriendo menú interactivo de la hamburguesería...")
print("¡Bienvenido!")
while True:
    print("Ingrese la acción que desea realizar:")
    print("[1] Agregar un pedido")
    print("[2] Ver historial de pedidos")
    try:
        opcion = int(input("Ingresar opción:"))
        if opcion == 1:
            print("Rellene los datos:")
            comensal = input("Comensal:")
            mesa = input("Mesa:")
            lista_pedidos = os.listdir("POO EJERCICIO 2/PEDIDOS")
            
            chequeo_menu(lista_pedidos, mesa)
            pedido = Pedido(comensal, mesa)
            producto = elegir_menu()
            pedido.agregar_producto(producto)
            database = pedido.to_dict()
            guardar_datos(database)
    except ValueError:
        print("¡Igrese un número válido!")