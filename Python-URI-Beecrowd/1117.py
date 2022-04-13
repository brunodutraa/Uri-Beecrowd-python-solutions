n = notas = 0
while n != 2:
    nota = float(input())
    if nota < 0 or nota > 10:
        print('nota invalida')
    else:
        notas += nota
        n += 1
print(f'media = {notas/2:.2f}')
