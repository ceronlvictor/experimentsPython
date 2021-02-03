class Campo:

    def __init__(self):
        self.coordenadas_de_borrachos = {} #Coordenadas de los borerachos

    def añadir_borracho(self, borracho, coordenada): #Añadimos al borracho
        self.coordenadas_de_borrachos[borracho] = coordenada #Ubicación del borracho

    def mover_borracho(self, borracho): #Movimineto
        delta_x, delta_y = borracho.camina() #Obtenemos el objeto de coordenada
        coordenada_actual = self.coordenadas_de_borrachos[borracho]  # Del objeto Coordenada ejecutamos el método mover con los parámetros
        nueva_coordenada = coordenada_actual.mover(delta_x, delta_y)

        self.coordenadas_de_borrachos[borracho] = nueva_coordenada

    def obtener_coordenada(self, borracho):
        return self.coordenadas_de_borrachos[borracho]

