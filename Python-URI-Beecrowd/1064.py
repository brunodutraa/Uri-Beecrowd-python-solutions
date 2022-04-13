positivos = 0
soma = 0

for c in range(6):
    n = float(input())
    if n > 0:
        positivos = positivos + 1
        soma = soma + n

print(positivos,  'valores positivos')
print('{:.1f}'.format(soma / positivos))
