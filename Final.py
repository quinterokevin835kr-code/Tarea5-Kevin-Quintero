productos = []

cantidad = int(input("Ingrese la cantidad de productos: "))

for i in range(cantidad):
    print("\nRegistro del producto", i + 1)

    referencia = int(input("Digite el codigo del producto: "))
    nombre_producto = input("Digite el nombre del producto: ")
    existencia = int(input("Digite la cantidad disponible: "))
    minimo = int(input("Digite el stock minimo permitido: "))

    productos.append([referencia, nombre_producto, existencia, minimo])

def revisar_stock(actual, minimo):
    pedido = 0

    if actual < minimo:
        pedido = minimo - actual

    return pedido

print("\nREPORTE DE ABASTECIMIENTO")
print("=" * 40)

for dato in productos:
    codigo = dato[0]
    nombre = dato[1]
    stock = dato[2]
    stock_minimo = dato[3]

    resultado = revisar_stock(stock, stock_minimo)

    print("Codigo:", codigo)
    print("Producto:", nombre)
    print("Stock disponible:", stock)
    print("Stock minimo:", stock_minimo)

    if resultado > 0:
        print("Se deben pedir:", resultado)
    else:
        print("No es necesario realizar pedido")

    print("=" * 40)