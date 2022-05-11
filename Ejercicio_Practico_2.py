print("******************************************************\n* Programa que determina si un número es par o impar *\n******************************************************")

num = int(input("Por favor, introduce un número entero: "))

comprobacion = num % 2

if comprobacion == 0:
    print("El número ", num, "es par.")
else:
    print("El número ", num, "es impar.")
