import random
import math

def media(X):
    return sum(X) / len(X) #Sumamos todos los valores y los dividimos entre la cnatidad de valores

def varianza(X):
    mu = media(X) #Igualamos la media 

    acumulador = 0 #Esta variable irá guardando los valores de la diferencia entre cada uno de los valores menos la media 

    for x in X:
        acumulador += (x - mu)**2
    
    return acumulador / len(X) #Acumlador entre la longitud de X

def desviacion_estandar(X):
    return math.sqrt(varianza(X)) #Raiz curadra de los resultados obtenidos anteriormente


if __name__ == "__main__":
    X = [random.randint(9, 12) for i in range(20)]
    mu = media(X)
    Var = varianza(X)
    sigma = desviacion_estandar(X)

    print(f'Arreglo X {X}')
    print(f'Media {mu}')
    print(f'Varianza {mu}')
    print(f'Desviacioon Estandar =  {sigma}') 

    