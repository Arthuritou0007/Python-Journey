import json

class Pugil:
    def __init__(self, dni, nombre, gimnasio, peso, postura):
        self.dni = dni
        self.nombre = nombre
        self.gimnasio = gimnasio
        self.peso = peso
        self.postura = postura
        self.estado = "Pendiente" # El estado de aprobación
        
        # Estadísticas tipo Tapology
        self.victorias = 0
        self.derrotas = 0
        self.empates = 0
        self.historial_peleas = [] # Acá guardaremos diccionarios con cada pelea

    # EL TRADUCTOR
    def to_dict(self):
        return {
            "dni": self.dni,
            "nombre": self.nombre,
            "gimnasio": self.gimnasio,
            "peso": self.peso,
            "postura": self.postura,
            "estado": self.estado,
            "estadisticas": {
                "victorias": self.victorias,
                "derrotas": self.derrotas,
                "empates": self.empates,
                "total_peleas": self.victorias + self.derrotas + self.empates
            },
            "historial_peleas": self.historial_peleas
        }

datos_recuperados = 0

with open("boxeador_chamorro.json", "r", encoding="utf-8") as archivo:
    datos_recuperados = json.load(archivo)

boxeador_clon = Pugil(datos_recuperados["dni"], datos_recuperados["nombre"], datos_recuperados["gimnasio"], datos_recuperados["peso"], datos_recuperados["postura"])
boxeador_clon.historial_peleas.append(datos_recuperados["historial_peleas"][0])
boxeador_clon.victorias += 1
boxeador_clon.estado = datos_recuperados["estado"]
datos_para_guardar = boxeador_clon.to_dict()

with open("boxeador_clon.json", "w", encoding="utf-8") as archivo:
    
    json.dump(datos_para_guardar, archivo, indent=4, ensure_ascii=False)