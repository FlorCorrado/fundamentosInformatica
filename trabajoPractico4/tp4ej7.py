valorIngresado = int(input("Ingrese un valor, para salir ingrese -1: "))
mayorNumero = 0
menorNumero = valorIngresado

while valorIngresado != -1:
    if valorIngresado > mayorNumero:
        mayorNumero = valorIngresado
        valorIngresado = int(input("Ingrese un valor, para salir ingrese -1: "))
    elif valorIngresado < menorNumero:
        menorNumero = valorIngresado
        valorIngresado = int(input("Ingrese un valor, para salir ingrese -1: "))
    else:
        valorIngresado = int(input("Ingrese un valor, para salir ingrese -1: "))


print("El mayor numero ingresado fue: ", mayorNumero)
print("El menor numero ingresado fue: ", menorNumero)
