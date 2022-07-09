resta = int(input())
tempo_presentes = input().split()
total = int(tempo_presentes[0]) + int(tempo_presentes[1])
if total > resta:
    print('Deixa para amanha!')
else:
    print('Farei hoje!')
