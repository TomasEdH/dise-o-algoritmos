import random

aciertos = 0
fallos = 0
usuario = input('¿cual es tu nombre?: ')
fallos_respuestas = []

def validarNumero():
    while True:
        try:
            inputPregunta = input(f'¿cuanto es el resultado de {numeroRandom} x {numeroRandom1}?: ')
            return int(inputPregunta)
        except ValueError:
            print('ingresa un numero valido')


while aciertos < 10 or fallos < 10:
    numeroRandom = random.randint(1, 10)
    numeroRandom1 = random.randint(1, 10)
    preguntarMultiplicacion = validarNumero()
    if numeroRandom * numeroRandom1 == preguntarMultiplicacion:
        aciertos += 1
        if aciertos == 1:
            print(f'\033[92mcorrecto, llevas {aciertos} acierto\033[0m')
        else:
         print(f'\033[92mcorrecto, llevas {aciertos} aciertos\033[0m')
    else:
        fallos += 1
        fallos_respuestas.append(f'{numeroRandom} x {numeroRandom1} = {preguntarMultiplicacion}, la respuesta correcta era {numeroRandom * numeroRandom1}')
        if fallos == 1:
            print(f'\033[91mincorrecto, la respuesta correcta era {numeroRandom * numeroRandom1}, llevas {fallos} fallo\033[0m')
        print(f'\033[91mincorrecto, la respuesta correcta era {numeroRandom * numeroRandom1}, llevas {fallos} fallos\033[0m')
        
    if aciertos == 10:
        print(f'\033[94mganaste, {usuario}\033[0m')
        break
    elif fallos == 10:
        print(f'\033[93mperdiste porque tienes mas de 10 fallos, {usuario}\033[0m')
        print('Tus respuestas incorrectas son: ')
        for i in fallos_respuestas:
         print(i)
        break
    
    

    
        