musicas = {'PROXYCITY': 0, 'P.Y.N.G.': 1, 'DNSUEY!': 2, 'SERVERS': 3, 'HOST!': 4, 'CRIPTONIZE': 5,
           'OFFLINE DAY': 6, 'SALT': 7, 'ANSWER!': 8, 'RAR?': 9, 'WIFI ANTENNAS': 10}

n = int(input())
for c in range(n):
    n1, n2 = map(int, input().split())
    total = n1 + n2
    for musica, valor in musicas.items():
        if valor == total:
            print(musica)
