n = int(input())
for c in range(0, n):
    notas = input().split()
    n1 = float(notas[0])
    n2 = float(notas[1])
    n3 = float(notas[2])
    media = (2 * n1 + 3 * n2 + 5 * n3)/10
    print('{:.1f}'.format(media))
