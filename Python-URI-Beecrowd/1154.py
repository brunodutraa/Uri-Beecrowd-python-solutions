lista = []
continua = True
soma = 0
while continua:
    idade = int(input())
    if idade >= 0:
        lista.append(idade)
    else:
        continua = False
for c in range(len(lista)):
    soma += lista[c]
print('{:.2f}'.format(soma / int(len(lista))))
