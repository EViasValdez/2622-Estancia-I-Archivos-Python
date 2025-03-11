Nombre = input("Ingrese el nombre del cliente ")
ValorCompra = float(input("Ingrese el valor de la compra "))
Descuento = float(ValorCompra * Descuento)

if ValorCompra < 80:
     print(f"Hola, {Nombre}. El valor a pagar es: $ {ValorCompra}")
elif 80 <= ValorCompra < 150:
      Descuento = 0.1
elif 150 <= ValorCompra <= 300:
      Descuento = 0.15
elif 300 <= ValorCompra < 500:
      Descuento = 0.2

PrecioFinal = ValorCompra - (ValorCompra * Descuento)
print(f"Compra sin descuento: {ValorCompra} . \n Compra con descuento: {PrecioFinal}")