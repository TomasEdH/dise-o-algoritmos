Algoritmo SistemaVotacion
    Definir candidatos, voto, totalVotos, ganador Como Entero
    Definir nombreCandidato Como Cadena
	
    candidatos <- 3  // Puedes cambiar este valor según la cantidad de candidatos
    Dimension nombres[candidatos]
    Dimension votos[candidatos]
	
    // Inicializar votos a 0
    Para i <- 1 Hasta candidatos Hacer
        votos[i] <- 0
    FinPara
	
    // Ingresar nombres de los candidatos
    Para i <- 1 Hasta candidatos Hacer
        Escribir "Ingrese el nombre del candidato ", i, ": "
        Leer nombres[i]
    FinPara
	
    Escribir "Bienvenido al sistema de votación"
	
    // Ingresar votos
    Repetir
        voto <- -1 // Inicializar voto con un valor inválido
        Mientras voto < 0 O voto > candidatos Hacer
            Escribir "Por favor, seleccione el número del candidato por el que desea votar (1-", candidatos, "), o ingrese 0 para salir: "
            Leer voto
            Si voto < 0 O voto > candidatos Entonces
                Escribir "Número de candidato inválido. Inténtelo de nuevo."
            FinSi
        FinMientras
		
        Si voto > 0 Entonces
            votos[voto] <- votos[voto] + 1
        FinSi
    Hasta que voto = 0
	
    // Calcular total de votos y encontrar al ganador
    totalVotos <- 0
    ganador <- 1
    Para i <- 1 Hasta candidatos Hacer
        totalVotos <- totalVotos + votos[i]
        Si votos[i] > votos[ganador] Entonces
            ganador <- i
        FinSi
    FinPara
	
    // Mostrar resultados
    Escribir "Total de votos emitidos: ", totalVotos
    Escribir "El ganador es ", nombres[ganador], " con ", votos[ganador], " votos."
	
FinAlgoritmo

