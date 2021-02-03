import random

class Borracho:
    
    def __init__(self, nombre):
        self.nombre = nombre


class BorrachoTradicional(Borracho):
    #Definición del borracho
    def __init__(self, nombre):
        super().__init__(nombre)

    def camina(self):
        return random.choice([(0, 1), (0, -1), (1,0), (-1,0)]) #Representación de las coordenadas
        # son las posibilidades de movimeinto
#Creación de una instancias 
"""class BorrachoTradicional(Borracho):
    #Atributos de la instancia
    def __init__(self, nombre):
        #El nombre dentro de la instancia son los parametros 
        super().__init__(nombre)
    #Metodo de la instancia 
    def camina(slef):
        return random.choice([(random.random(),random.random()**2), (random.random(), random.random()**-2), (random.random()**2, random.random()), (random.random()**-2,random.random())])"""