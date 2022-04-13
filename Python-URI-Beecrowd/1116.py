n = int(input())
for c in range(n):
    num = input().split()
    n1 = int(num[0])
    n2 = int(num[1])
    if n2 == 0:
        print('divisao impossivel')
    else:
        print(round(n1 / n2,  1))
