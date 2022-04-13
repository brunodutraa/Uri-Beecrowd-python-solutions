lados = input().split()
l1 = float(lados[0])
l2 = float(lados[1])
l3 = float(lados[2])
if l1 >= l2 and l1 >= l3:
    a = l1
    b = l2
    c = l3
if l2 >= l1 and l2 >= l3:
    a = l2
    b = l1
    c = l3
if l3 >= l1 and l3 >= l2:
    a = l3
    b = l1
    c = l2
if a >= b + c:
    print('NAO FORMA TRIANGULO')
else:
    if a**2 == (b**2+c**2):
        print('TRIANGULO RETANGULO')
    if a**2 > (b**2+c**2):
        print('TRIANGULO OBTUSANGULO')
    if a**2 < (b**2+c**2):
        print('TRIANGULO ACUTANGULO')
    if a == b and a == c and b == c:
        print('TRIANGULO EQUILATERO')
    if (a == b and a != c) or (a == c and a != b) or (b == c and c != a):
        print('TRIANGULO ISOSCELES')
