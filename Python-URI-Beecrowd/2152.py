n = int(input())
for c in range(n):
    h, m, o = map(int, input().split())
    if h < 10:
        print(str(h).rjust(2, '0'), end='')
    else:
        print(h, end='')
    print(':', end='')
    if m < 10:
        print(str(m).rjust(2, '0'), end=' - ')
    else:
        print(m, end=' - ')
    if o == 1:
        print('A porta abriu!')
    else:
        print('A porta fechou!')