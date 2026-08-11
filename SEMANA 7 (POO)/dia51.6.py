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

        datos_para_guardar = self.to_dict()

        with open(f"boxeador_{self.dni}.json", "w", encoding="utf-8") as archivo:
            json.dump(datos_para_guardar, archivo, indent=4, ensure_ascii=False)

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

    def actualizar(self, dni):
        datos_recuperados = 0
                    
        with open(f"boxeador_{dni}.json", "r", encoding="utf-8") as archivo:
            datos_recuperados = json.load(archivo)

        