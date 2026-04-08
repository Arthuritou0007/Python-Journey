def calcular_precio(cantidad, pérdida, valor_original, ganancia):
    cantidad_total = cantidad - pérdida
    precio_costo = valor_original / cantidad_total
    porcentaje = (ganancia / 100) + 1
    final = precio_costo * porcentaje
    return round(final, 2)

def pedir_numero(mensaje):
   while True:
      try:
         valor = float(input(mensaje))
         if valor >= 0:
            return valor
         else:
            print("¡Error! No se admiten números negativos.")
            continue
      except ValueError:
         print("¡Error! Ingrese un dato válido.")

while True:
   print("¡Hola! Bienvenido a la calculadora de precios.")
   print("¿Quiere calcular un precio por unidad o por KGs?")
   print("1. Por KG.")
   print("2. Por Unidad.")
   
   while True:
      respuesta = pedir_numero("Ingrese su respuesta aquí: ")

      if respuesta == 1:
         cantidad = pedir_numero("Ingrese cuántos KGs pesó el producto: ")
         break
      elif respuesta == 2:
         cantidad = pedir_numero("Ingrese la cantidad de frutos: ")
         break
      else:
         print("¡Error! Ingrese una respuesta válida.")
         continue

   if respuesta == 1:
      pérdida = pedir_numero("Ingrese la cantidad de pérdida en KGs: ")
   else:
      pérdida = pedir_numero("Ingrese la cantidad de pérdida en unidades: ")
   
   valor_original = pedir_numero("Ingrese cuánto le costó el producto: $")
   ganancia = pedir_numero("Ingrese el porcentaje de ganancia que quiere agregar: ")

   if respuesta == 1:
      try:
         print(f"El valor por KG de su producto es de: ${float(calcular_precio(cantidad, pérdida, valor_original, ganancia))}")
         print("¿Desea hacer otro cálculo?")
         print("1. Sí.")
         print("2. No.")

         while True:
            nueva_respuesta = int(pedir_numero("Ingrese su respuesta: "))

            if nueva_respuesta == 1:
               break
            elif nueva_respuesta == 2:
               break
            else:
               print("¡Ingrese un dato válido!")
               continue
      except ZeroDivisionError:
         print("¡Error! La pérdida no puede ser igual o mayor a la cantidad.")
         print("Reiniciando...")
         continue
   else:
      try:
         print(f"El valor por Unidad de su producto es de: ${float(calcular_precio(cantidad, pérdida, valor_original, ganancia))} c/u")
         print("¿Desea hacer otro cálculo?")
         print("1. Sí.")
         print("2. No.")

         while True:
            nueva_respuesta = int(pedir_numero("Ingrese su respuesta: "))

            if nueva_respuesta == 1:
               break
            elif nueva_respuesta == 2:
               break
            else:
               print("¡Ingrese un dato válido!")
               continue
      except ZeroDivisionError:
         print("¡Error! La pérdida no puede ser igual o mayor a la cantidad.")
         print("Reiniciando...")
         continue
   if nueva_respuesta == 2:
      break