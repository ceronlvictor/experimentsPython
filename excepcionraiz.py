import math 
def raiz_cuadrada_elementos_lista(lista, multiplicador):
    try:
        return [math.sqrt(i*multiplicador) for i in lista]
    except ValueError as e:
        print (e)
        return f'no existe la raíz cuadrada de un negativo'    

lista = list(range(10))
multiplicador = -8

print (raiz_cuadrada_elementos_lista(lista, multiplicador))