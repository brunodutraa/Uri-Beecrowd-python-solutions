while True:
    try:
        jogada = input().split()
        empate = False
        ganhador = ''

        for e in jogada:
            if jogada.count(e) == 3:
                print('Putz vei, o Leo ta demorando muito pra jogar...')
                empate = True
                break
        if len(set(jogada)) == len(jogada):
            print('Putz vei, o Leo ta demorando muito pra jogar...')
            empate = True
        if not empate:
            lista_final = list(set(jogada))
            if 'pedra' in lista_final and 'tesoura' in lista_final:
                if jogada.count('pedra') == 2:
                    print('Putz vei, o Leo ta demorando muito pra jogar...')
                else:
                    ganhador = 'pedra'

            elif 'pedra' in lista_final and 'papel' in lista_final:
                if jogada.count('papel') == 2:
                    print('Putz vei, o Leo ta demorando muito pra jogar...')
                else:
                    ganhador = 'papel'

            elif 'tesoura' in lista_final and 'papel' in lista_final:
                if jogada.count('tesoura') == 2:
                    print('Putz vei, o Leo ta demorando muito pra jogar...')
                else:
                    ganhador = 'tesoura'
            if ganhador != '':
                if jogada.index(ganhador) == 0:
                    print('Os atributos dos monstros vao ser inteligencia, sabedoria...')
                elif jogada.index(ganhador) == 1:
                    print("Iron Maiden's gonna get you, no matter how far!")
                elif jogada.index(ganhador) == 2:
                    print('Urano perdeu algo muito precioso...')
    except EOFError:
        break
