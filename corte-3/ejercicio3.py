recipientes = [int(input("ingrese la cantidad de palillos para el recipiente 1 entre 1 y 100: ")),
                   int(input("ingrese la cantidad de palillos para el recipiente 2 entre 1 y 100: "))]

jugador_actual = 1
while True:
        print("\nrecipiente 1:", recipientes[0])
        print("recipiente 2:", recipientes[1])

        if jugador_actual == 1:
            print("\nturno del jugador 1")
        else:
            print("\nturno del jugador 2")
            
        recipiente = int(input("seleccione el recipiente 1 o 2: "))
        if recipiente != 1 and recipiente != 2:
            print('Tiene que escoger un recipiente entre 1 o 2')
            continue

        cantidad = int(input("ingrese la cantidad de palillos a quitar 1-" + str(recipientes[recipiente - 1]) + "): "))
        if cantidad < 1 or cantidad > recipientes[recipiente - 1]:
            print(f"\033[93mtiene que escoger una cantidad entre 1 y {recipientes[recipiente - 1]} palillos\033[0m")
            continue

        recipientes[recipiente - 1] -= cantidad

        if recipientes[0] == 0 and recipientes[1] == 0:
            print(f"\n\033[92mEl jugador {jugador_actual} ganó\033[0m")
            break
        jugador_actual = 1 if jugador_actual == 2 else 21


