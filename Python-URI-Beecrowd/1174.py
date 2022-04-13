lista = []
for c in range(100):
    n = float(input())
    lista.append(n)
    if n <= 10:
        print('A[{}] = {}'.format(c, n))
