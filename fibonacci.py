"""def fib_iter(n):
        a=0
        b=1
        for i in range(n):
            c=a+b
            a=b
            b=c 
        return b
for x in range(20):
    print(f"Iteracion, {fib_iter(x)}")"""

#Forma de Recursividad 

def fib_rec(r):
    if r < 2:
        return r
    return fib_rec(r-1) + fib_rec(r-2)
for y in range(20):
    print(f"{fib_rec(y)}, Recursividad")