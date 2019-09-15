numeroComparacion = int(input("Ingrese un numero: "))
numeroIngresado = int(input("Ingrese un numero: "))
resultado = ""

while numeroIngresado != -1:
    if numeroIngresado < numeroComparacion:
        resultado = resultado + str(numeroIngresado) + " "
    numeroIngresado = int(input("Ingrese un numero: "))

print("Los numeros ingresados menores al numero de comparacion son: ", resultado)

