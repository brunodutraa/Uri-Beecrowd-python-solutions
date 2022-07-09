n = int(input())
matriculas = []
notas = []
maior8 = False
for c in range(n):
    aluno = input().split()
    matriculas.append(int(aluno[0]))
    notas.append(float(aluno[1]))
    if float(aluno[1]) >= 8:
        maior8 = True
if not maior8:
    print('Minimum note not reached')
else:
    maior_nota = max(notas)
    indice = notas.index(maior_nota)
    print(matriculas[indice])
