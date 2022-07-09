n = int(input())

for c in range(n):
    n1 = input()
    n2 = input()
    lista = [n1, n2]
    if 'ataque' in lista and 'papel' in lista:
        if n1 == 'ataque':
            print('Jogador 1 venceu')
        else:
            print('Jogador 2 venceu')
    elif 'pedra' in lista and 'papel' in lista:
        if n1 == 'pedra':
            print('Jogador 1 venceu')
        else:
            print('Jogador 2 venceu')
    elif 'ataque' in lista and 'pedra' in lista:
        if n1 == 'ataque':
            print('Jogador 1 venceu')
        else:
            print('Jogador 2 venceu')
    elif n1 == n2:
        if n1 == 'ataque':
            print('Aniquilacao mutua')
        elif n1 == 'papel':
            print('Ambos venceram')
        elif n1 == 'pedra':
            print('Sem ganhador')
