def puede_subir(altura, edad):
    if altura < 120 or edad < 10:
        return False
    else:
        return True
    
print("¡Hola! Para ingresar debe proporcionar los siguientes datos:")

altura_dada = int(input("Ingrese su altura en cm: "))
edad_dada = int(input("Ingrese su edad: "))

puede = puede_subir(altura_dada, edad_dada)

if puede == True:
    print("¡Puedes subir!")
else:
    print("Lo siento, no tienes permitido subir.")