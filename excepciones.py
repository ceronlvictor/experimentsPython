def divide_elementos_de_una_lista(lista, divisor):
    try:
        return [i / divisor for i in lista]
    except ZeroDivisionError as e:
        print(e)
        return lista


lsita = list(range(10))
divisor = 0
print(divide_elementos_de_una_lista(lsita, divisor))