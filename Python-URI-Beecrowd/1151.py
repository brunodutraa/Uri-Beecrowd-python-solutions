n = int(input())
n1 = 0
n2 = 1
if n ==1:
    print(n1)
if n == 2:
    print(n1,end=' ')
    print(n2)
if n >= 3:
    print(n1,end = ' ')
    print(n2,end = ' ')
    for c in range(n - 2):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        if c == n-3:
            print(n3)
        else:
            print(n3, end=' ')