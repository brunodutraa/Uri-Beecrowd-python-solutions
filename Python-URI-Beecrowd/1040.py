notas = input().split()
media = (2 * float(notas[0]) + 3 * float(notas[1]) + 4 * float(notas[2]) + 1 * float(notas[3])) / 10
if media >= 7:
   print('Media: {:.1f}'.format(media))
   print('Aluno aprovado.')
elif media < 5:
    print('Media: {:.1f}'.format(media))
    print('Aluno reprovado.')
else:
    print('Media: {:.1f}'.format(media))
    print('Aluno em exame.')
    exame = float(input())
    print('Nota do exame: {:.1f}'.format(exame))
    media_final = (media + exame) / 2
    if media_final >= 5:
        print('Aluno aprovado.')
        print('Media final: {:.1f}'.format(media_final))
    else:
        print('Aluno reprovado.')
        print('Media final: {:.1f}'.format(media_final))
