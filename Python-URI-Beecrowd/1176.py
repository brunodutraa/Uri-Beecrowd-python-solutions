n = int(input())
for c in range(n):
    termo = int(input())
    f = [0, 1]
    if termo <= 1:
        print('Fib({}) = {}'.format(termo, f[termo]))
    else:
        for d in range(2, termo + 1):
            f.append(f[d - 1] + f[d - 2])
        print('Fib({}) = {}'.format(termo, f[termo]))
