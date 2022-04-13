while True:
    n = input().split()
    if n == ['0','0']:
        break
    total = int(n[1]) - int(n[0])
    notas = [2, 5, 10, 20, 50, 100]
    possivel = False
    total_parcial = 0
    for num in notas:
        for num2 in notas:
            total_parcial = num + num2
            if total_parcial == total:
                possivel = True
                break
            if total_parcial > total:
                break
    if possivel:
        print('possible')
    else:
        print('impossible')
