print("**************************************** \n* Sistema de control vacacional Rappi. *\n****************************************\n")

nombre = input("Por favor, ingrese el nombre del operario que desea consultar: ")
print("")
años = int(input("Ahora ingrese los años totales trabajados por el operario: "))
print("")
clave = int(input("Por último, introduzca la clave de identificación del operario, identificándolo como: '1 (atención al cliente), 2 (logística), o 3 (gerencia): "))

if clave == 1:
    if años == 1:
        print("\n" + nombre + ": Adquiere 6 días de vacaciones.")
    elif años > 1 and años < 7:
        print("\n" + nombre + ": Adquiere 14 días de vacaciones.")
    elif años > 7:
        print("\n" + nombre + ": Adquiere 20 días de vacaciones.")
    else:
        print("\n" + nombre + ": Sin derecho a vacaciones.")
elif clave == 2:
    if años == 1:
        print("\n" + nombre + ": Adquiere 7 días de vacaciones.")
    elif años > 1 and años < 7:
        print("\n" + nombre + ": Adquiere 15 días de vacaciones.")
    elif años > 7:
        print("\n" + nombre + ": Adquiere 22 días de vacaciones.")
    else:
        print("\n" + nombre + ": Sin derecho a vacaciones.")
elif clave == 3:
    if años == 1:
        print("\n" + nombre + ": Adquiere 10 días de vacaciones.")
    elif años > 1 and años < 7:
        print("\n" + nombre + ": Adquiere 20 días de vacaciones.")
    elif años > 7:
        print("\n" + nombre + ": Adquiere 30 días de vacaciones.")
    else:
        print("\n" + nombre + ": Sin derecho a vacaciones.")
else:
    print("La clave no existe.")    

print("Fin.")
