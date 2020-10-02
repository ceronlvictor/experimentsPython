def primo(numero):
    contador = 0
    while(contador<=numero):
        if i==1 or i==numero:  
          continue 
        if numero %i ==0:
            contador+=1
    if contador ==0:
        return True
    else:
        return False

def run():
    numero = int(input("Write a number: "))
    if primo(numero):
        print("The numer is prime")
    else:
        print("The numer is not prime")
if __name__ == "__main__":
    run()