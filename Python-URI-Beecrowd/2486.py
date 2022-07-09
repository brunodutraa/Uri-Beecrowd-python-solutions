alimentos = {'sucodelaranja': 120, 'morangofresco': 85, 'mamao': 85, 'goiabavermelha': 70,
             'manga': 56, 'laranja': 50, 'brocolis': 34}
while True:
    total = 0
    n = int(input())
    if n == 0:
        break
    for c in range(n):
        numero = []
        palavra = []
        a = list(input())
        for letra in a:
            if letra.isnumeric():
                numero.append(letra)
            elif letra != ' ':
                palavra.append(letra)
        numero = ''.join(numero)
        numero = int(numero)
        palavra = ''.join(palavra)
        for q, almto in alimentos.items():
            if q == palavra:
                total += numero * almto
    if 110 <= total <= 130:
        print(f'{total} mg')
    elif total > 130:
        print(f'Menos {total - 130} mg')
    elif total < 110:
        print(f'Mais {110 - total} mg')
