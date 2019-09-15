a = int(input("Por favor, ingrese un valor, para salir escriba -1: "))
b = ""
primerValorIngresado = a

while a != -1:
    b = a
    a = int(input("Por favor, ingrese un valor, para salir escriba -1: "))

print("El primer número ingresado fue: ", primerValorIngresado)
print("El último número ingresado fue: ", b)
