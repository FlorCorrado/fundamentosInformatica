numeroIngresado = int(input("Ingrese un número para evaluar si es par o impar, para salir ingrese -1: "))
numerosPares = ""
numerosImpares = ""

while numeroIngresado != -1:
    if numeroIngresado % 2 == 0:
        numerosPares = numerosPares + str(numeroIngresado) + " "
        numeroIngresado = int(input("Ingrese un número para evaluar si es par o impar, para salir ingrese -1: "))
    else:
        numerosImpares = numerosImpares + str(numeroIngresado) + " "
        numeroIngresado = int(input("Ingrese un número para evaluar si es par o impar, para salir ingrese -1: "))

print("Los números pares ingresados fueron: ", numerosPares)

print("Los números impares ingresados fueron: ", numerosImpares)
