#Ejemplo 1

nombre, edad = input("Ingresa tu nombre: "), input("Ingresa tu edad: ")

print("\nHola {}, ¿qué tal va todo?, actualmente tienes {} años de edad.".format(nombre, edad))

#Ejemplo 2 (Declaro el nombre de la variable que deseo usar pertenecientes a 'format' dentro de los corchetes '{}')

print("\nHola {nombre}, ¿qué tal va todo?, actualmente tienes {edad} años de edad.".format(nombre = input("Ingresa tu nombre: "), edad = input("Ingresa tu edad: ")))

#Ejemplo 3 (Declaro la posición de la variable que deseo usar pertenecientes a 'format' dentro de los corchetes '{}')

nombre, edad = input("Ingresa tu nombre: "), input("Ingresa tu edad: ")

print("\nHola {1}, ¿qué tal va todo?, actualmente tienes {0} años de edad.".format(edad, nombre))