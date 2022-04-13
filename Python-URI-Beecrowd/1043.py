def istriangule(a,b,c):
    if a < b+c and b < a+c and c < a+b:
        return True
    else:
        return False


medidas = input().split()
a = float(medidas[0])
b = float(medidas[1])
c = float(medidas[2])
if istriangule(a,b,c):
    perimetro = a+b+c
    print(f'Perimetro = {perimetro:.1f}')
else:
    area = ((a+b)*c)/2
    print(f'Area = {area:.1f}')
