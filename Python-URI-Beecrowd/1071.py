soma = 0
n1 = int(input())
n2 = int(input())
if n1 > n2:
    for c in range(n2 + 1, n1):
        if c % 2 != 0:
            soma += c
else:
    for c in range(n1+1, n2):
        if c % 2 != 0:
            soma += c
print(soma)