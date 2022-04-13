maior = posicao = 0
for c in range(1, 101):
    n = int(input())
    if n > maior:
        maior = n
        posicao = c
print(maior)
print(posicao)
