class coordenada:
""" Definimos la clase, con ello inicializamos las instancias, seguido de esto definicmos el motodo que vamos a 
usar para las operaciones, finalmante asignamos los atributos de las instancias"""
    def __init__(self, x, y):#Definicion de clases
        self.x = x
        self.y = y 

    def distancia(self, otra_coordenada): #definicion de metodo
        x_diff = (self. x - otra_coordenada.x)**2 #Metodos 
        y_diff = (self.y - otra_coordenada.y)**2

        return (x_diff + y_diff)**0.5

if __name__ == '__main__':

    coord_1 = coordenada(3, 30) #Instancias 
    coord_2 = coordenada(4, 8)

    #print(coord_1.distancia(coord_2))
    print(isinstance(3, coordenada)) #metodo para saber si es una instancia de la clase