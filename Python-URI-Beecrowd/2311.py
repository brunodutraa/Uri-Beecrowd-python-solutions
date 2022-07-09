n = int(input())
for c in range(n):
    nome = input()
    dific = float(input())
    pontos = input().split()
    pontos_float = []
    pontos_map = []
    for ponto in pontos:
        pontos_float.append(float(ponto))
    pontos_map = [ponto for ponto in pontos_float if not ponto == max(pontos_float) and not ponto == min(pontos_float)]
    print(f'{nome} {sum(pontos_map) * dific:.2f}')
