print("Calculadora con una sola variable.\n")

print("********************")
print("* Menú de opciones *")
print("********************")

print("""1. Suma
2. Resta
3. Multiplicación
4. División
5. División entera
6. Exponente
7. Módulo o Resto""")

numero = int(input("Introduce la operación deseada: "))

if numero == 1:        
    print("Elegiste 'Suma'.\n")
    numero = int(input("Introduce el primer número: "))
    numero += int(input("Introduce el segundo número: "))
    print("\nEl resultado de la Suma es:", numero)

elif numero == 2:
    print("Elegiste 'Resta'.\n")
    numero = int(input("Introduce el primer número: "))
    numero -= int(input("Introduce el segundo número: "))
    print("\nEl resultado de la Resta es:", numero)
    
elif numero == 3:
    print("Elegiste 'Multiplicación'.\n")
    numero = int(input("Introduce el primer número: "))
    numero *= int(input("Introduce el segundo número: "))
    print("\nEl resultado de la Multiplicación es:", numero)

elif numero == 4:
    print("Elegiste 'División'.\n")
    numero = float(input("Introduce el primer número: "))
    numero /= float(input("Introduce el segundo número: "))
    print("\nEl resultado de la División es:", round(numero, 2))
    
elif numero == 5:
    print("Elegiste 'División entera'.\n")
    numero = int(input("Introduce el primer número: "))
    numero //= int(input("Introduce el segundo número: "))
    print("\nEl resultado de la División entera es:", numero)
    
elif numero == 6:
    print("Elegiste 'Exponente'.\n")
    numero = int(input("Introduce el primer número: "))
    numero **= int(input("Introduce el segundo número: "))
    print("\nEl resultado del Exponente es:", numero)

elif numero == 7:
    print("Elegiste 'Módulo o Resto'.\n")
    numero = int(input("Introduce el primer número: "))
    numero %= int(input("Introduce el segundo número: "))
    print("\nEl resultado del Módulo o Resto es:", numero)

else:
    print("La opción ingresada no es válida.")
