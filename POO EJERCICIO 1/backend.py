import json
import os

def guardar_datos(datos):
    with open(f"POO EJERCICIO 1/DATABASE/{datos['nombre']}.json", "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

def cargar_datos(nombre_mascota):
    with open(f"POO EJERCICIO 1/DATABASE/{nombre_mascota}", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
        return datos

def obtener_lista_pacientes():
    lista_archivos = os.listdir("POO EJERCICIO 1/DATABASE")
    return lista_archivos