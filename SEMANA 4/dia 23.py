def pedir_numero_entero(mensaje):
   while True:
      try:
         valor = int(input(mensaje))
         return valor
      except ValueError:
         print("¡Error! Ingrese un dato válido.")
      

ganancia = pedir_numero_entero("Ingrese la ganancia que desea: ")
pérdida = pedir_numero_entero("Ingrese la pérdida en KGs: ")

print(pérdida, ganancia)