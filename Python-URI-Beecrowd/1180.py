n = int(input())
listain = input().split()
lista = []
for numero in listain:
    lista.append(int(numero))
menor = min(lista)
print(f'Menor valor: {menor}')
print(f'Posicao: {lista.index(menor)}')
