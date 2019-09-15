a = int(input("Por favor, ingrese un número para saber si es par o impar, para salir escriba -1: "))

while a != -1:
    if a%2 == 0:
        print("El número ingresado es par")
        a = int(input("Por favor, ingrese un número para saber si es par o impar, para salir escriba -1: "))
    else:
        print("El número ingresado es impar")
        a = int(input("Por favor, ingrese un número para saber si es par o impar, para salir escriba -1: "))
