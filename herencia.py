#Modelar una Jerarquia de Clase en donde se comparta el comportamiento de la clase

class Rectangulo: #GEneramos una clase 
    def __init__(self, base, altura ): #Inicializamos la clase con el constuctor 
        self.base = base#le asignamos variables de instancia 
        self.altura = altura
    
    def area(self):#metodo que nos clacula el area
        return self.base * self.altura

class Cuadrado(Rectangulo): #LA clase cuadrado extiende a la clase rectangulo

    def __init__(self, lado):
        super().__init__ (lado, lado) #pemite obtener una referencia de la primer clase (Rectangulo)

if __name__ == "__main__":
    rectangulo = Rectangulo(base = 3, altura = 4)
    print(rectangulo.area())

    cuadrado = Cuadrado(lado = 5)
    print(cuadrado.area())#Estamos implementandoo el metodo area en una clase en la que no esta definido 
    #Estamos heredando el metodo área 

