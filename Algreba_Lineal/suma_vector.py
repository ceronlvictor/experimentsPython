import numpy as np
rojo = [255,0,0]
negro = [0,0,0]

#Debemos conciderar que si solo sumamos vectores, python nos devuelve una concatenaciónn
print('rojo + negro resulta en',rojo+negro)


#Sin embargo podemos aplicar una funcón para realizar la suma:
def suma_vectores(a,b):
    return [i+j for i,j in zip(a,b)]

print('suma_vectores(rojo,negro) nos devuelve',suma_vectores(rojo,negro))


#Sin embargo esto no es practico a lo largo por ello implementamos numpy
print('\n_'*3)
rojo = np.array(rojo)
negro = np.array(negro)

#Tipo del array
print(type(rojo))

#Numpy nos permite realizar la suma de vectores
print('\nLa suma de los numpy array rojo + negro es', rojo+negro)

#ejercicio 
#Sean  a=(1,2,3,4,5) ,  b=(−1,−2,−3,−4,5)  y  c=a+b=(0,0,0,0,10) . Vamos a replicar este cálculo en Python con ayuda de numpy.
a = np.array([1,2,3,4,5]) #declaramos el arreglo/vector a
b = np.array([-1,-2,-3,-4,5]) #declaramos el arreglo/vector b

c = a+b
print('La el vector c = a+b =',c)
