a = int(input("Ingrese un valor númerico: "))
ultimoValorNum = 0
valorImpar = 0
b = 0

while a != -1:
    b = int(input("Ingrese un valor númerico: "))
    if b != -1:
        ultimoValorNum = b
        a = int(input("Ingrese un valor númerico: "))
    else:
        a = -1


print("El ultimo valor ingresado en una posicion par fue: ", ultimoValorNum)
