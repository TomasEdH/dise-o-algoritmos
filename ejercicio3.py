
recipientes = [int(input("Ingrese la cantidad de palillos para el recipiente 1 (1-100): ")),
                   int(input("Ingrese la cantidad de palillos para el recipiente 2 (1-100): "))]

jugador_actual = 1
while True:
        print("\nRecipiente 1:", recipientes[0])
        print("Recipiente 2:", recipientes[1])

        if jugador_actual == 1:
            print("\nTurno del jugador 1")
        else:
            print("\nTurno del jugador 2")
            
        recipiente = int(input("Seleccione el recipiente (1 o 2): "))
        if recipiente != 1 and recipiente != 2:
            print("Recipiente inválido. Por favor, seleccione 1 o 2.")
            continue

        cantidad = int(input("Ingrese la cantidad de palillos a quitar (1-" + str(recipientes[recipiente - 1]) + "): "))
        if cantidad < 1 or cantidad > recipientes[recipiente - 1]:
            print("Cantidad inválida. Por favor, ingrese una cantidad válida.")
            continue

        recipientes[recipiente - 1] -= cantidad

        if recipientes[0] == 0 and recipientes[1] == 0:
            print("\n¡El jugador", jugador_actual, "ha ganado!")
            break
        jugador_actual = 1 if jugador_actual == 2 else 2


