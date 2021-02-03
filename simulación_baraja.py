import random
import collections



PALOS = [ 'espada', 'corazon', 'rombo', 'trebol']
VALORES  = ['as', '2', '3', '4', '5', '6', '7', '8', '9', 'jota', 'reina', 'rey']
#Funcion para generar la baraja
def crear_baraja():
    barajas = []
    for palo in PALOS:
        for valor in VALORES:
            barajas.append((palo, valor))
    
    return barajas

def obtener_mano(barajas, tamano_mano):
    mano = random.sample(barajas, tamano_mano)

    return mano

def main(tamano_mano, intentos):
    barajas = crear_baraja()

    manos = []

    for _ in range(intentos):
        mano = obtener_mano(barajas, tamano_mano)
        manos.append(mano)

    pares = 0
    for mano in manos:
        valores = []
        for carta in mano:
            valores.append(carta[1]) #tenems el valor uno porque en las tuplas el valor 0 es el de palo, y el 1 es el de valor
        counter = dict(collections.Counter(valores))
        for val in counter.values():
            if val == 3:
                pares += 1
                break

    probabilidad_par = pares / intentos
    print(f'La probabilidad de obtener un par en una mano de {tamano_mano} barajas es {probabilidad_par}')







if __name__ == '__main__':
    #El usuario nos indica el tamaño de la mano
    tamano_mano = int(input('De cuantas barajas sera la mano: '))
    intentos = int(input('Cuantos intentos para calcular la probabilidad: '))
    #Nos indica cuantas veces vamos a correr la simulacion
    main(tamano_mano, intentos)