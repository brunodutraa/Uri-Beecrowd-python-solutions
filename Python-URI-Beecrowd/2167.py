n = int(input())
lista = list(map(int, input().split()))

queda = maior = 0
tam = int(len(lista))
for c in range(1, n):
    if lista[c] < lista[c-1]:
        print(c+1)
        queda = True
        break
if not queda:
    print(0)
