import json
import os

def guardar_datos(datos):
    with open(f"POO EJERCICIO 2/PEDIDOS/Mesa_{datos['mesa']}.json", "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

def cargar_datos(mesa):
    with open(f"POO EJERCICIO 2/PEDIDOS/{mesa}.json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
        return datos