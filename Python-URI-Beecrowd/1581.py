n = int(input())
for c in range(n):
    idiomas = []
    casos = int(input())
    for d in range(casos):
        idiomas.append(input())
    if len(set(idiomas)) != 1:
        print('ingles')
    else:
        print(idiomas[0])
