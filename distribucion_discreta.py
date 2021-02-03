from math import factorial
# definición de la distribución binomial 
def my_binomial(k, n, p):
  return factorial(n)/(factorial(k)*(factorial(n-k)))*pow(p,k)*pow(1-p, n-k)

# escribe tu codigo aquí:
total = 0
for n in range(0,3):
  total += my_binomial(n,6,0.5)
 
print(total) 