numeroDado = int(input("Ingrese un número: "))
resultado = 1
factorial = 0

while numeroDado > 1:
    if numeroDado == 0:
        print("El numero tiene que ser mayor a 0")
        break
    resultado = resultado * numeroDado
    numeroDado = numeroDado - 1


print("El factorial del número es: ", resultado)
