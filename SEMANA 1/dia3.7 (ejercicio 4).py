precio = 1000
descuento = 0.3
recargo = 0.1

precio_descontado = precio - (precio * descuento)
precio_final = precio_descontado + (precio_descontado * recargo)

print("PRECIO DEL PRODUCTO:", precio)
print("DESCUENTO: 30%")
print("RECARGO DE ENVÍO: 10%")  
print("PRECIO FINAL:", precio_final)