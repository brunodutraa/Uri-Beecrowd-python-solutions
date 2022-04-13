n = int(input())
for c in range(n):
    bonus = int(input())
    dabriel = input().split()
    guarte = input().split()
    v_dabriel = (int(dabriel[0]) + int(dabriel[1])) / 2
    v_guarte = (int(guarte[0]) + int(guarte[1])) / 2
    if int(dabriel[2]) % 2 == 0:
        v_dabriel += bonus
    if int(guarte[2]) %2 == 0:
        v_guarte += bonus
    if v_guarte > v_dabriel:
        print('Guarte')
    elif v_guarte < v_dabriel:
        print('Dabriel')
    else:
        print('Empate')
