n = int(input())
lista = []
t = 0
while t < 1000:
    for c in range(n):
        if len(lista) < 1000:
            lista.append(c)
            print('N[{}] = {}'.format(t, c))
            t += 1
