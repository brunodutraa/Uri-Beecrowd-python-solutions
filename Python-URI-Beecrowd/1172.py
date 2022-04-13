x = [1,2,3,4,5,6,7,8,9,10]
for c in range(len(x)):
    n = int(input())
    if n <= 0:
        x[c] = 1
    else:
        x[c] = n
    print('X[{}] = {}'.format(c, x[c]))
