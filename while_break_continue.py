def run():
    # contador=0
    # while(contador<100):
    #     contador=contador+1
    #     if contador+8==95:
    #         break
    #     print(contador)
    contador=0
    while(contador<50):
        contador=contador+1
        if contador==10:
            continue
        elif contador==47:
            break
        else:
            print(contador)
        
if __name__ == '__main__':
    run()