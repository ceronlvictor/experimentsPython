import math

def distance(x1,y1,x2,y2):
    sq1 = (x1-x2)*(x1-x2)
    sq2 = (y1-y2)*(y1-y2)
    return math.sqrt(sq1 + sq2)

if __name__ == "__main__":
    x1 = int(input('Ingrese la cordenada en x: '))
    x2 = int(input('Ingrese la cordenada en x: '))
    y1 = int(input('Ingrese la cordenada en x: '))
    y2 = int(input('Ingrese la cordenada en x: '))
    distanceB = distance(x1,y1,x2,y2)
    print(distanceB)