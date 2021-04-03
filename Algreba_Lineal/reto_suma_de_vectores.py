import numpy as np

rojo = np.array([255,0,0])
verde = np.array([0,255,0])
a = np.array([0,0,255])
negro = np.array([0,0,0])

#¿Qué color obtienes si sumas  rojo + verde + a
uno = rojo + verde + a
print('La suma de los tres vectores es: ', uno)
#¿Qué color obtienes sumando rojo + verde?
dos = rojo + verde
print(dos)
#¿Qué color obtienes sumando  negro − a  ? ¿Tiene sentido este resultado dentro del modelo aditivo RGB?
tres = negro - a
print (tres)

#Blanco, Amarillo y el tercero es un número sin sentido.
#El modelo RGB es una forma de representar colores como luces, es por eso 
# que el negro es (0 0 0) ausencia completa de luz y el blanco es (255 255 255) todas 
# las luces al máximo. Los números entre 0 y 255 representan la cantidad de luz emitida por el color y cualquier numero
#  fuera del rango no tiene sentido en este sistema.
