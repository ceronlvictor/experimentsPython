
import random #Importamos random para implemetar numeros aleatorios

def busqueda_lineal(lista, objeto): #Función para buscar dentro de una lista
    match = False #variable para identificar si un objeto está dentro de una lsita

    for elemento in lista:
        a += 1
        if elemento == objetivo:
            macth == True 
            break 
        return match 

if __name__ == "__main__":
    tamaño_de_lista = int(input('De que tamano es la lista?')) #Le pregunramos al ususario de que tamaño es la lista que quiere ocupar
    objetivo = int(input('Que numero quieres encontrar?')) #PReguntamos cual numero quiere buscar dentro de la lista

    lista = [random.randint(0, 100) for i in range (tamaño_de_lista)]
    print('La función se tardo {a} veces')
    encontrado = busqueda_lineal(lista, objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista') #comparamos si encontrado esta dentro de la lista 

 


