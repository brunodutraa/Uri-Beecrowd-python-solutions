n = int(input())
aux = 1
pum = 4
for c in range(1, 4*n+1):
    if c != pum:
        print(c,end=' ')
    else:
        print('PUM')
        pum += 4
