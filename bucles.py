# contador = 0
# print("la potencia de 2 elevado a " + str (contador) + " es: "+str(2**contador))

# contador = 1
# print("la potencia de 2 elevado a " + str (contador) + " es: "+str(2**contador))

# contador = 2
# print("la potencia de 2 elevado a " + str (contador) + " es: "+str(2**contador))

# contador = 3
# print("la potencia de 2 elevado a " + str (contador) + " es: "+str(2**contador))


# contador = 4
# print("la potencia de 2 elevado a " + str (contador) + " es: "+str(2**contador))

# contador = 5
# print("la potencia de 2 elevado a " + str (contador) + " es: "+str(2**contador))

def run():
    LIMITE=1000
    contador=0
    potencia_2 = 2**contador
    while potencia_2<LIMITE:
        print("la potencia de 2 elevado a " + str (contador) + " es: "+str(potencia_2))
        contador=contador+1
        potencia_2 = 2 **contador


if __name__=='__main__':
    run()