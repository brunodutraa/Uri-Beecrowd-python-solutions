n = int(input())
lista = []
for c in range(10):
    lista.append(n)
    print('N[{}] = {}'.format(c, n))
    n = n * 2
