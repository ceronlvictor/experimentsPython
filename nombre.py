def run():

    nombre = input('¿Cual es tu nombre?: ')
    print("Hola buen dia " + nombre)
    v = "El tamaño de tu nombre es: "
    print("El tamaño de tu nombre es "  +str(len(nombre)))

if __name__ == "__main__":
    run()