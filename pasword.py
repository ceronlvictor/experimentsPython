import random


def paswordgeneratos():
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    simbolos  = ['(', ')', '$', '%', '!', '&', '/', '#']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    caracteres = mayusculas + minusculas + simbolos + numeros
    pasword = []

    for i in range(15):
        caracter_random = random.choice(caracteres)
        pasword.append(caracter_random)
    
    pasword=''.join(pasword)
    return pasword

def run():
    pasword = paswordgeneratos()
    print('Tu nueva contrañesa es: ' + pasword)

if __name__ == "__main__":
    run()