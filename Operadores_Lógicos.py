#Conjunción

print("Conjunción (and)")

num_uno = int(input("Escribe un número mayor a 2 y menor a 5: "))

if num_uno > 2 and num_uno < 5:
    print("\n El número que elegiste cumple las propiedades.\n")
else:
    print("\n El número que elegiste no cumple las propiedades.\n")

#Disyunción
print("Disyunción (or)")

palabra = input("Para cumplir con la condición escribe 'si' o 'yes': ")

if palabra == "si" or palabra == "yes":
    print("\n La condición se ha cumplido.\n")
else:
    print("\n La condición NO se ha cumplido.\n")

#Negación
    print("Negación (not)\n")

num_uno = int(input("Introduce un número diferente a 5: "))

if not num_uno == 5:
    print("\n El número es diferente de cinco y SI cumple la condición. \n")
else:
    print("\n El número es igual a cinco y no cumple la condición.\n")
