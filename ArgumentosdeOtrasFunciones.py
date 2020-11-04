def multiplicar_por_dos(n):
    return n * 2

def sumar_dos(n):
    return n + 2

def aplicar_operacion(f, numeros): #Esta función toma los aprametros de entrada, ejecuta la funcion y guarda los resultados
    resultados = [] #Se crea un arreglo 
    for numero in numeros:  #Variable iteradora
        resultado = f(numero)   #Es ejecutada la función utilizando uno de los parametros y es guardada en resultada
        resultados.append(resultado)    #Se va guardando el resultado de cada iteración. 
    return resultados  

>>> nums = [1, 2, 3]
>>> aplicar_operacion(multiplicar_por_dos, nums) #La función es invocada 
[2, 4, 6]

>>> aplicar_operacion(sumar_dos, nums)
[3, 4, 5]
