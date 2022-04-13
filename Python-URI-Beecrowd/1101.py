soma = 0
while True:
    n = input().split()
    n1 = int(min(n))
    n2 = int(max(n))
    if n1 <= 0 or n2 <= 0:
        break
    for c in range(n1, n2+1):
        soma += c
        print(c, end=' ')
    print(f'Sum={soma}')
    soma = 0
