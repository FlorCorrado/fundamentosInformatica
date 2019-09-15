numeroIngresado = 1
numerosImpares = ""

while 1 <= numeroIngresado <= 1000:
    if numeroIngresado % 2 != 0:
        numerosImpares = numerosImpares + str(numeroIngresado) + " "
        numeroIngresado = numeroIngresado + 1
    else:
        numeroIngresado = numeroIngresado + 1

print(numerosImpares)
print("Fin")
