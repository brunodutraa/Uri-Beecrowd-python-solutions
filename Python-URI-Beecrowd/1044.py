n = input().split()
n1 = int(n[0])
n2 = int(n[1])
if n1 > n2:
    if n1 % n2 == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')
else:
    if n2 % n1 == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')
