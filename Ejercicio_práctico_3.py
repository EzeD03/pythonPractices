print("***************************************************************************")
print("* Programa para determinar ¿Cuál es el número más grande de tres números? *")
print("***************************************************************************")

num_uno = int(input("Introduzca el primer número a comparar: "))
num_dos = int(input("Introduzca el segundo número a comparar: "))
num_tres = int(input("Introduzca el tercer número a comparar: "))

max_num = max([num_uno,num_dos,num_tres])

print("El número más grande introducido es el: ", max_num)
