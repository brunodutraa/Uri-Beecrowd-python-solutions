while True:
    try:
        lista = [['1'],['1'], ['A','B','C'], ['D','E','F'], ['G','H','I'], ['J','K','L'], ['M','N','O'], ['P','Q','R','S'], ['T','U','V'], ['W','X','Y','Z']]
        entrada = input().upper()
        lista_geral = []
        for digito in entrada:
            if digito.isalpha() or digito.isnumeric() or digito in '*#':
                lista_geral.append(digito)

        for elemento in lista_geral:
            if elemento.isnumeric():
                print(elemento,end='')
            elif elemento in '*#':
                print(elemento, end='')
            else:
                for ind, conj in enumerate(lista):
                    if elemento in conj:
                        print(ind,end='')
        print()

    except EOFError:
        break
