pi = 3.14159
abc = input().split()
a = float(abc[0])
b = float(abc[1])
c = float(abc[2])
print(f'TRIANGULO: {a * c / 2:.3f}')
print(f'CIRCULO: {pi * c**2:.3f}')
print(f'TRAPEZIO: {(a + b)/2 * c:.3f}')
print(f'QUADRADO: {b * b:.3f}')
print(f'RETANGULO: {a * b:.3f}')
