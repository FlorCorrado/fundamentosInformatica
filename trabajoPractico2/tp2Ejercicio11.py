valorBinario = input("Ingrese un número binario de 4 dígitos: ")

numDecimal = int(valorBinario, 2)

numero1 = int(valorBinario[0])
numero2 = int(valorBinario[1])
numero3 = int(valorBinario[2])
numero4 = int(valorBinario[3])

valorFinal = 2**3 * numero1 + 2**2 * numero2 + 2**1 * numero3 + 2**0 * numero1

print("El valor binario ingresado en decimal equivale a ", numDecimal)
print("El valor binario ingresado en decimal equivale a ", valorFinal)
