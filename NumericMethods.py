"""def busqueda_binaria(objetivo)
    epsilon = 0.001
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - objetivo) >= epsilon:
        print(f'bajo = {bajo}, alto{alto}, respuesta{respuesta}')
        if respuesta**2 < objetivo:  
            bajo = respuesta
        else: 
            alto = respuesta 
    
    respuesta = (alto + bajo) / 2

    #print(f'La raiz cuadrada de {objetivo} es {respuesta}')
return f{'La raiz cuadrada de {objetivo} es {respuesta}'}"""
print(f'Aproximación exahustiva (1) Busqueda Binaria (2) ')
metodo = int(input('Escoge una opción; '))
if metodo ==  1:
        objetivo = int(input('Escoge un numero: '))
        epsilon = 0.001
        paso = epsilon**2
        respuesta = 0.0

        while abs(respuesta**2 -objetivo) >= epsilon and respuesta <= objetivo:  
            print(abs(respuesta**2 - objetivo), respuesta)
            respuesta += paso 

        if abs(respuesta**2 - objetivo) >= epsilon: 
            print(f'No se encontro la raiz cuadrada de {objetivo}')
        else:
            print(f'La raiz cuadrada de {objetivo} es la {respuesta}')
if metodo == 2:
        objetivo = int(input('Escoge un numero: '))
        epsilon = 0.001
        bajo = 0.0
        alto = max(1.0, objetivo)
        respuesta = (alto + bajo) / 2

        while abs(respuesta**2 - objetivo) >= epsilon:
            print(f'bajo = {bajo}, alto{alto}, respuesta{respuesta}')
            if respuesta**2 < objetivo:  
                bajo = respuesta
            else: 
                alto = respuesta 
    
            respuesta = (alto + bajo) / 2

        print(f'La raiz cuadrada de {objetivo} es {respuesta}')