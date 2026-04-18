class Boxeador:
    # El molde pide los datos al momento de crearse
    def __init__(self, peso_ingresado, edad_ingresada, peleas_ingresadas, estatura_ingresada):
        # El objeto (self) se guarda los datos en su propio diccionario interno
        self.peso = peso_ingresado
        self.edad = edad_ingresada
        self.peleas = peleas_ingresadas
        self.estatura = estatura_ingresada

    # La acción que sabe hacer
    def tirar_jab(self):
        return "¡Pum! Jab rápido."