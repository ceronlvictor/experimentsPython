def ordenamiento_por_insercion(lista): #Definimos la función 

    for indice in range(1, len(lista)): #indice (posisicón dentro de la lista)
        valor_actual = lista[indice] #Variable para asignar la posicion dentro de la lsita 
        posicion_actual = indice #Variable para asignar la posición dentro de la lista 

        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual: 
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1

        lista[posicion_actual] = valor_actual