"""Lanzamientos de dados
Comenzamos estableciendo los posibles valores que puede tormar Simulación de aleatoridad
Calculamos la media, 
Graficamos la media"""

import random

def lanzamiento_dados(numero_de_lanzamientos):
    valor_de_los_dados = []
    
    for _ in range(numero_de_lanzamientos):
        dado = random.choice([1,2,3,4,5,6])
        tiro = dado
        valor_de_los_dados.append(tiro)
        print(f'El valor del dado es: {tiro}')

if __name__ == "__main__":
    numero_de_lanzamientos = int(input('¿Cuantos lanzamientos quieres realizar?: '))
    lanzamiento_dados(numero_de_lanzamientos)


