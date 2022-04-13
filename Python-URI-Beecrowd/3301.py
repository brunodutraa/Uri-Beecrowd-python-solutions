idades = input().split()
meio = ''
for idade in idades:
    if idade != min(idades) and idade != max(idades):
        meio = idade
indice = idades.index(meio)
if indice == 0:
    print('huguinho')
elif indice == 1:
    print('zezinho')
else:
    print('luisinho')
