import random 

def ordenamiento_por_mezcla(lista): 
    if len(lista) > 1:  #Parte 1 comenzamos haciendo en paquetes nuestra lista
        medio = len(lista) // 2 #PArtimos a la mitad nuestra lista
        izquierda = lista[:medio]   #parte izquierda del punto incial a la mitad
        derecha = lista[medio:] #Parte derecha del punto medio al punto final 
        print(izquierda, '-'*20, derecha)

        # llmada recursiva
        ordenamiento_por_mezcla(izquierda) #Esta llamada a recursividad permite que la función vaya partiendo la lista una y otra vez
        ordenamiento_por_mezcla(derecha)

        #Iteradores para recorrer las sublista
        i = 0
        j = 0
        #Iterador para movernos dentro de la lista principal
        k = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            
            k += 1

            while i < len(izquierda):
                lista[k] = izquierda[i]
                i += 1
                k += 1

            while j < len(derecha):
                lista[k] = derecha[j]
                j += 1
                k += 1
            print(f'izquierda {izquierda}, derecha {derecha}')
            print(lista)
            print('-'*100)
            return lista

if __name__ == '__main__': 
        tamano_de_lista = int(input('De que tamaño es la lista? '))
        lista = [random.randint(0, 100) for i in range(tamano_de_lista)]
        print(lista)
        print('-'*100)

        lista_ordenada = ordenamiento_por_mezcla(lista)
        print(lista_ordenada)
    