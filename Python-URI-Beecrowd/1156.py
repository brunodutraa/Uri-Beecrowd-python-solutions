soma = 0
j = 1
for c in range(1, 40, 2):
    soma = float(soma + c / j)
    j *= 2
print('{:.2f}'.format(soma))
