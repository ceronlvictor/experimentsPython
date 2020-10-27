'''x = 0.0
for i in range(10):
    x +=0.1

if x == 100:
    print(f' x = {x}')
else:
    print(f'x != {x}')'''

objetivo = int(input('Escoge un entero: '))
respuesta = 0

while respuesta**2 < objetivo:
    respuesta += 1 

if respuesta**2 == objetivo: 
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')
else: 
    print(f'{objetivo} no tienen raiz cuadrada')