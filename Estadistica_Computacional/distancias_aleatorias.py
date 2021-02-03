from borra_aleatory import BorrachoTradicional #Importamos la instancia BorrachoTradicional (con ello toddos sus atributos)
from campo import Campo #Importamos la clase campo con todas sus instancias y metodos
from coordenada import Coordenada #Importamos la clase coordenada  (Abastracción del espacio donde se encuentra el borracho)
from bokeh.plotting import figure, show

""" Grafia los caminos hechos por el borracho

Ingresamos la simulación de un borracho 
Mmedimos las distancias 
Trazamos el camino  
Graficamos"""

def caminata(campo, borracho, pasos):
    inicio = campo.obtener_coordenada(borracho) #Colocamos a nuestro borracho en el inicio 

    for _ in range(pasos): #función para hacer moverse al borracho
        campo.mover_borracho(borracho)

    return inicio.distancia(campo.obtener_coordenada(borracho)) #Devolvemos las coordenadas 

def simular_caminata(pasos, numero_de_intentos, tipo_de_borracho): #Simualación de la caminata, le ingresamos los parametros pasos, numero de intentos (cantidad de repeticion) y el tipo de vborracho

    borracho =  tipo_de_borracho(nombre = 'Hector') #la función recibe un borrachop
    origen = Coordenada(0,0) #Empezamos en el origen 
    distancias = [] #Creamos un arreglo de las distancias

    for _ in range(numero_de_intentos): #Ciclo para repetir el numero de intentos 
        campo = Campo() 
        campo.añadir_borracho(borracho, origen)
        simular_caminata = caminata(campo, borracho, pasos) #
        distancias.append(round(simular_caminata, 1)) #Metodo para agregar nuevos elementos a la lista 
    return distancias

def graficar(x, y):
    grafica = figure(title = 'Camino aleatorio', x_axis_label = 'Pasos', y_axis_label = 'Desplazamiento')
    grafica.line(x,y, legend = 'distancia media')

    show(grafica)

def main(campo, borracho, distancias):
    x_arreglo = []
    y_arreglo = []

    x_arreglo.append(campo.obtener_coordenada(borracho).x)
    y_arreglo.append(campo.obtener_coordenada(borracho).y)

    for _ in distancias:
        campo.mover_borracho(borracho)

    x_arreglo.append(campo.obtener_coordenada(borracho).x)
    y_arreglo.append(campo.obtener_coordenada(borracho).y)




if __name__ == "__main__":
    distancias_de_caminata = [10, 100, 1000, 10000] 
    numero_de_intentos = 200 #Numero de intnetos de la simulación

    main(campo, borracho, distancias)