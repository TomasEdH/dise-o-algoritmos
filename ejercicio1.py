total = 0

while total >= 30:
    jugador_1 = input('Jugador 1 ingresa un numero del 1 al 3: ')
    if jugador_1 >= 1 and jugador_1 <= 3:
        total += jugador_1
        if total >= 30:
            print('Jugador 1 es el ganador')
            break
    else:
        print('Ingresa un numero valido')
    
    jugador_2 = input('Jugador 2 ingresa un numero del 1 al 3: ')
    if jugador_2 >= 1 and jugador_2 <= 3:
        total += jugador_2
        if total >= 30:
            print('Jugador 2 es el ganador')
            break
    else:
        print('Ingresa un numero valido')
        


    
    