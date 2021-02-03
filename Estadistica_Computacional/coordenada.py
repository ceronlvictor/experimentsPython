class Coordenada: #Abastracción del espacio donde se encuentra el borracho
    
    def __init__(self, x, y):
        self.x = x #Inciializamos x
        self.y = y #Inciializamos y

    def mover(self, delta_x, delta_y): #Mover la posición
        return Coordenada(self.x + delta_x, self.y + delta_y)#Devuelve los cambios realizados (movimeinto)

    def distancia(self, otra_coordenada): #Metodo de pitagorás para calcuñar la distancia.
        delta_x = self.x - otra_coordenada.x #Cambio en x
        delta_y = self.y - otra_coordenada.y #Cambio en y

        return (delta_x**2 + delta_y**2)**0.5 #Debolvemos la distancia 