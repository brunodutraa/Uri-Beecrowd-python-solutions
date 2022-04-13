n = int(input())
for c in range(n):
    joao = maria = 0
    for d in range(3):
        joao_lista = input().split()
        joao += int(joao_lista[0]) * int(joao_lista[1])
    for d in range(3):
        maria_lista = input().split()
        maria += int(maria_lista[0]) * int(maria_lista[1])
    if joao > maria:
        print('JOAO')
    else:
        print('MARIA')
