class Lavadora:

    def __init__(self):
        pass

    def lavar(self, temperatura = 'caliente'): #metodo publico 
        self._llenar_tanque_de_agua(temperatura)#INicializamos las variables 
        self._añadir_jabon()#NOrmalmente estos metodos no le interesan al usuario
        self._lavar()
        self._centrifugar()

    def _llenar_tanque_de_agua(self, temperatura):
        print(f'Llenando el tanque de agua {temperatura}')

    def _añadir_jabon(self):
        print('Añadiendo Jabon')
    
    def _lavar(self):
        print('lavando la ropa')

    def _centrifugar(self):
        print('Centrifugando la ropa')


if __name__ == '__main__':
    lavadora = Lavadora() 
    lavadora.lavar()

