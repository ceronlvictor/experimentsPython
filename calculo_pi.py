import random
import math
from media import desviacion_estandar, media

def aventar_agujas(numero_de_ajugas): #Funcion que hace la simulación del lanzamiento de las ajugas
    adentro_del_circulo = 0 

    for _ in range(numero_de_ajugas):  #Concideración del numero de ajugas 
        x = random.random() * random.choice([-1, 1]) #Simulación aleatoria del valor que tomara en la posición x
        y = random.random() * random.choice([-1, 1]) 
        distancia_desde_el_centro = math.sqrt(x**2 + y**2) #Distancia entre la aguja lanzada y el origen 

        if distancia_desde_el_centro <= 1: #Si la distancia es menor a 1 implica que está dentro del area del circulo
            adentro_del_circulo += 1 #Variable 
    return (4 * adentro_del_circulo) / numero_de_ajugas


def estimacion(numero_de_ajugas, numero_de_intentos):
    estimados = []
    for _ in range(numero_de_intentos):
        estiamacion_pi = aventar_agujas(numero_de_ajugas)
        estimados.append(estiamacion_pi)

    media_estimados = media(estimados)
    sigma = desviacion_estandar(estimados)
    print(f'Estimación de Pi = {round(media_estimados, 15)}, Sigma(Desviacion estandar) = {round(sigma, 5 )}, Ajugas = {numero_de_ajugas}')
     
    return (media_estimados, sigma)

def estimar_pi(precision, numero_de_intentos):
    numero_de_ajugas = 1000
    sigma = precision #Criterio de parada buscamos que el 95 de nuestros datos tengan el 0.01 de presicion 

    while sigma>= precision / 1.96:
        media, sigma = estimacion(numero_de_ajugas, numero_de_intentos)
        numero_de_ajugas *= 2 #Aumento de las ajugas 


    return media


if __name__ == '__main__':
    estimar_pi(0.01, 1000)





