n = int(input())
for c in range(n):
    soma = 0
    num = int(input())
    for f in range(1, num):
        if num % f == 0:
            soma += f
    if soma == num:
        print(f'{num} eh perfeito')
    else:
        print(f'{num} nao eh perfeito')
