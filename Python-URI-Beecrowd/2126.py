caso = 1
while True:
    try:
        teste = input()
        teste2 = input()
        teste_i = str(teste[::-1])
        teste2_1 = str(teste2[::-1])
        ind_final = repet = 0
        if teste in teste2:
            repet = teste2_1.count(teste_i)
            ind_teste = teste2_1.index(teste_i)
            ind_final = len(teste2_1) - (ind_teste - 1) - len(teste_i)
            print(f'Caso #{caso}:\nQtd.Subsequencias: {repet}\nPos: {ind_final}')
        else:
            print(f'Caso #{caso}:\nNao existe subsequencia')
        caso += 1
        print()
    except EOFError:
        break
