Las SQL son distintas a los diccionarios, guardan la información de forma distinta a los .json

En éste día estudié esa lógica y creé éste esquema para practicar:
Producto
- id (1)
- nombre (Hamburguesa clasica)
- precio (5000)
- categoría (Hamburguesas)

Producto
- id (2)
- nombre (Coca cola)
- precio (2000)
- categoría (Bebida)

Mesa
- id (3)
- número (3)
- estado (habilitado)
- capacidad (2 personas)

Pedido
- id (4)
- mesa_id (3)
- fecha (07/11)
- estado (en preparación)

DetallePedido
- id (5)
- pedido_id (4)
- producto_id (1)
- cantidad (2)
- precio (5000)

DetallePedido
- id (6)
- pedido_id (4)
- producto_id (2)
- cantidad (1)
- precio (2000)