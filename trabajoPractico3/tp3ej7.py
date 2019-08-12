productosVendidosOriginales = int(input("Ingrese el número de productos vendidos: "))
precioBase = int(input("Ingrese el precio base del producto: "))
precioCon10Descuento = precioBase - (precioBase * 0.10)
precioCon25Descuento = precioBase - (precioBase * 0.25)
precioTotal = 0
productosVendidos = productosVendidosOriginales

productosVendidosRestantes = productosVendidos - 100
if productosVendidosRestantes > 0:
    precioTotal = productosVendidosRestantes * precioCon25Descuento
    productosVendidos = 100

productosVendidosRestantes = productosVendidos - 12

if productosVendidosRestantes > 0:
    precioTotal += productosVendidosRestantes * precioCon10Descuento
    productosVendidos = 12

precioTotal += productosVendidos * precioBase

print("El valor total de la venta es de: ", precioTotal)
print("El precio promedio por venta es de: ", precioTotal/productosVendidosOriginales)
