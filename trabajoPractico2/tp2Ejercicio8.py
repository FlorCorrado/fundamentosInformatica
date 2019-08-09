
vendedor = int(input("Ingrese el número de vendedor: "))
salarioParcial = 800
ventas = int(input("Ingrese la cantidad de libros vendidos por el vendedor: "))
comision = ventas * 50
valorTotalVentas = int(input("Ingrese el valor total de las ventas realizadas por el vendedor: "))
comisionValorVentas = valorTotalVentas * 0.05

salarioTotal = salarioParcial + comision + comisionValorVentas

print("Al vendedor numero", vendedor, "le corresponde el salario total de: ", salarioTotal)
