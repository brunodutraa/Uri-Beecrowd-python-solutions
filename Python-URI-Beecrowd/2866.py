n = int(input())
for t in range(n):
    frase = input()
    frase_sep= list(frase)
    tam = len(frase)
    lista = []
    for c in range(tam):
        letra = frase_sep[c]
        if letra.islower():
            lista.append(letra)
            result = [''.join(lista)]
    print(result[0][::-1])
