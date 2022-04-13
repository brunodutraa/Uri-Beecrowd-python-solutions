n1 = int(input())
n2 = int(input())
s = 0
if n1 < n2:
    for c in range(n1, (n2 + 1)):
        if c % 13 != 0:
            s = s + c
    print(s)
else:
    for c in range(n2, (n1 + 1)):
        if c % 13 != 0:
            s = s + c
    print(s)
