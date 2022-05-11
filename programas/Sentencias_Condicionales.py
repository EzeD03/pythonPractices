print("Sistema para calcular el promedio de un alumno.")
name = input("Para comenzar, ¿Cuál es tu nombre?: ")

mat = int(input("¿Cuál es tu calificación en matemáticas?: "))

qui = int(input("¿Cuál es tu calificación en química?: "))

bio = int(input("¿Cuál es tu calificación en biología?: "))

promedio = (mat + qui + bio) / 3


if promedio > 6.5:
    print("¡Felicidades, " + name + " has aprobado la cursada con un promedio de ", promedio, "!.")
    print("Fin.")
else:
    print("Lastimosamente, " + name + " has desaprobado la cursada con un promedio de ", promedio, ".")
    print("Fin.")
