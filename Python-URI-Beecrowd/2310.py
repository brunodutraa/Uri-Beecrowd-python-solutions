n = int(input())
tot_s = tot_b = tot_a = tot_s1 = tot_b1 = tot_a1 = 0
for c in range(n):
    nome = input()
    s, b, a = map(int, input().split())
    tot_s += s
    tot_b += b
    tot_a += a
    s1, b1, a1 = map(int, input().split())
    tot_s1 += s1
    tot_b1 += b1
    tot_a1 += a1
print(f'Pontos de Saque: {100/tot_s * tot_s1:.2f} %.')
print(f'Pontos de Bloqueio: {100/tot_b * tot_b1:.2f} %.')
print(f'Pontos de Ataque: {100/tot_a * tot_a1:.2f} %.')
