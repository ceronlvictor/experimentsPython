from numpy import power
# función factorial
deffact(x):
  factorial = 1
  if int(x) >= 1:
    for i in range (1,int(x)+1):
      factorial = factorial * i
  return factorial
  
# distribución binomial 
defmy_binomial(k, n, p):
  return fact(n)/(fact(k)*(fact(n-k)))*power(p,k)*power(1-p, n-k)

# distribución binomial acumulada:
defbinom_acum(k,n,p):
  defmy_binomial(k, n, p):
    return fact(n)/(fact(k)*(fact(n-k)))*power(p,k)*power(1-p, n-k)
  acum = 0
  for i in range(k+1):
    acum += my_binomial(i,6,0.5)
  return acum