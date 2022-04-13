def raio(r):
    pi = 3.14159
    raio = (4.0/3) * pi * r**3
    return f'VOLUME = {raio:.3f}'
r = float(input())
print(raio(r))
