import random


def run():
    aleatry_number = random.randint(1,100)
    numberc = int(input("Elige un numero del 1 al 100: "))
    while numberc != aleatry_number:
        if numberc < aleatry_number:
            print("Busca un numero más grande")
        else:
            print("Busca un numero más pequeño")
        numberc = int(input("Elige un numero del 1 al 100: "))
    print("Ganaste!") 

if __name__=="__main__":
    run()