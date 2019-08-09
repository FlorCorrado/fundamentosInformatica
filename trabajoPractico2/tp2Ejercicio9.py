from math import trunc

cantDinero = int(input("Ingrese la cantidad de dinero a imprimir: "))

billetesCien = trunc(cantDinero / 100)
restoBilletesCien = cantDinero % 100

billetesCincuenta = trunc(restoBilletesCien / 50)
restoBilletesCincuenta = restoBilletesCien % 50

billetesDiez = trunc(restoBilletesCincuenta / 10)
restoBilletesDiez = restoBilletesCincuenta % 10

billetesCinco = trunc(restoBilletesDiez / 5)
restoBilletesCinco = restoBilletesDiez % 5

billetesUno = trunc(restoBilletesCinco / 1)


print("La cantidad de dinero a entregar es de ", billetesCien, "billetes de 100,", billetesCincuenta, "billetes de 50,",
      billetesDiez, "billetes de 10,", billetesCinco, "billetes de 5 y", billetesUno, "billetes de uno")
