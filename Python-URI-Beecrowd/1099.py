n = int(input())
for c in range(n):
    soma = 0
    num = input().split()
    n1 = int(num[0])
    n2 = int(num[1])
    if n1 > n2:
        for c in range(n2 + 1, n1):
            if c % 2 != 0:
                soma += c
    else:
        for c in range(n1 + 1, n2):
            if c % 2 != 0:
                soma += c
    print(soma)
