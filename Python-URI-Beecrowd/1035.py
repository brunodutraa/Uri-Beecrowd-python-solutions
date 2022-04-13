n = input().split()
a = int(n[0])
b = int(n[1])
c = int(n[2])
d = int(n[3])
if b > c and d > a and (c + d) > (a + b) and c > 0 and d > 0 and a % 2 == 0:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')
