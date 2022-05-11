mensaje = "Hola"
mensaje += " "
mensaje += "Ernesto"
print(mensaje)
print(" ")

print("Concatenación:")
mensaje = "Hola"
espacio = " "
nombre = "Ezequiel"
print(mensaje + espacio + nombre)
print(" ")

numero_uno = 4
numero_dos = 6
resultado = numero_uno + numero_dos
resultado = str(resultado)
print("El resultado de la suma es: " + resultado)
print(" ")

mensaje = "Hola Ezequiel"
print("Busqueda: ")
buscar_subcadena = mensaje.find("Ezequiel")
print(buscar_subcadena)
print(" ")

mensaje = "Hola Ezequiel"
extraer_subcadena = mensaje[0:8]
print(extraer_subcadena)
print(" ")

print("Comparación:")
mensaje_uno = "Hola Ernesto"
mensaje_dos = "Hola Ezequiel"
print(mensaje_uno == mensaje_dos)
print(" ")

print("Prueba de comparación de mensaje entre:")
mensaje = "Hola"
espacio = " "
nombre_uno = "Ernesto"
nombre_dos = "Ezequiel"
resultado_uno = mensaje + espacio + nombre_uno
resultado_dos = mensaje + espacio + nombre_dos
print(resultado_uno + " y " + resultado_dos)
print("Mensaje=" + mensaje)
extraer_subcadena_uno = resultado_uno [0:5]
extraer_subcadena_dos = resultado_dos [0:5]
print("El resultado de la prueba es:")
print(extraer_subcadena_dos == extraer_subcadena_uno)
