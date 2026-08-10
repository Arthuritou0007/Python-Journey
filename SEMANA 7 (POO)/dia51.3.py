import json

datos_recuperados = 0

with open("boxeador_chamorro.json", "r", encoding="utf-8") as archivo:

    datos_recuperados = json.load(archivo)

datos_recuperados["estado"] = "Aprobado"

with open("boxeador_chamorro.json", "w", encoding="utf-8") as archivo:
    json.dump(datos_recuperados, archivo, indent=4, ensure_ascii=False)
    print("Archivos guardados con éxito")

print(datos_recuperados)