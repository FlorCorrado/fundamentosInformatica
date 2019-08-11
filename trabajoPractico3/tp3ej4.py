num1 = int(input("Ingrese un número: "))

num2 = int(input("Ingrese otro número: "))

if num1 % num2 == 0:
    print("El número", num1, "es múltiplo de", num2)
elif num2 % num1 == 0:
    print("El número", num2, "es múltiplo de", num1)
else:
    print("Los números no son múltiplos")
