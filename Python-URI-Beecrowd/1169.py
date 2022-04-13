n = int(input())
for c in range(n):
    soma = 1
    quadrados = int(input())
    for d in range(quadrados):
        soma *= 2
    if soma / 12 / 1000 < 1:
        print('0 kg')
    else:
        print('{:.0f} kg'.format((soma / 12) // 1000))
