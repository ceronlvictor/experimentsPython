
from borra_aleatory import BorrachoTradicional #Importamos la instancia BorrachoTradicional (con ello toddos sus atributos)
from campo import Campo #Importamos la clase campo con todas sus instancias y metodos
from coordenada import Coordenada #Importamos la clase coordenada  (Abastracción del espacio donde se encuentra el borracho)
from bokeh.plotting import figure, show



def caminata(campo, borracho, pasos): #Metodo caminata los parametros que agregamos son campo, el borracho y la cantidad de pasos
    inicio = campo.obtener_coordenada(borracho) #Generamoos la coordenada del borracho

    for _ in range(pasos): #Ciclo para mover al borracho
        campo.mover_borracho(borracho)  #le pasamos el parametro borrcho a la funcion mover borracho dentro de programa campo 

    return inicio.distancia(campo.obtener_coordenada(borracho)) #Regresamos la variable  inciio, la cual la obtenemos de 
    #pasar el parametro borracho dentro de la funcion obtener coordenda, a este resultado lo pasamos por la función distancia. Para obtener la dis
    #tanjcia recorrida


def simular_caminata(pasos, numero_de_intentos, tipo_de_borracho): #Simualación de la caminata, le ingresamos los parametros pasos, numero de intentos (cantidad de repeticion) y el tipo de vborracho

    borracho =  tipo_de_borracho(nombre = 'Hector') #la función recibe un borrachop
    origen = Coordenada(0,0) #Empezamos en el origen 
    distancias = [] #Creamos un arreglo de las distancias

    for _ in range(numero_de_intentos): #Ciclo para repetir el numero de intenesto 
        campo = Campo() 
        campo.añadir_borracho(borracho, origen)
        simular_caminata = caminata(campo, borracho, pasos) #
        distancias.append(round(simular_caminata, 1)) #Metodo para agregar nuevos elementos a la lista 
    return distancias

def graficar(x, y):
    grafica = figure(title = 'Camino aleatorio', x_axis_label = 'pasos', y_axis_label = 'dsitancia')
    grafica.line(x,y, legend = 'Caminos')
    show(grafica)

       

def main(distancias_de_caminata, numero_de_intentos, tipo_de_borracho):
    distancias_media_por_caminata = []

    for pasos in distancias_de_caminata:
        distancias = simular_caminata(pasos, numero_de_intentos, tipo_de_borracho)
        distancia_media = round(sum(distancias)/ len(distancias),4)
        distancia_maxima = max(distancias)
        distancia_minima = min(distancias)
        distancias_media_por_caminata.append(distancia_media)
        print(f'{tipo_de_borracho.__name__} caminata aleatoria de {pasos}')
        print(f'media = {distancia_media}')
        print(f'Maxima = {distancia_maxima}')
        print(f'MIn = {distancia_minima}')
    graficar(distancias_de_caminata, distancias_media_por_caminata)

if __name__ == "__main__":
    distancias_de_caminata = [10, 100, 1000, 10000] 
    numero_de_intentos = 200 #Numero de intnetos de la simulación

    main(distancias_de_caminata, numero_de_intentos, BorrachoTradicional)

