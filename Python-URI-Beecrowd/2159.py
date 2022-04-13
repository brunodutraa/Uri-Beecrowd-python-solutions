from math import log
n = int(input())
minimo = n / log(n)
maximo = 1.25506 * minimo
print('{:.1f}'.format(minimo),end=' ')
print('{:.1f}'.format(maximo))
