from math import sqrt
while True:
    n = int(input())
    f = ((((1 + sqrt(5))/2)**n) - (((1 - sqrt(5))/2)**n)) / sqrt(5)
    print(f)
    print('%.1f' %f)
