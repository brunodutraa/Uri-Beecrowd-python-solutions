n = float(input())
lista = []
lista.append(n)
print('N[0] = {:.4f}'.format(n))
for c in range(1, 100):
    n = n / 2
    lista.append(n)
    print('N[{}] = {:.4f}'.format(c, n))
