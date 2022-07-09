for c in range(int(input())):
    fora_padrao = False
    placa = input()
    for letra in placa:
        if letra.islower():
            fora_padrao = True
            break

    if len(placa) != 8 or fora_padrao:
        print('FAILURE')
        continue

    if len(placa) == 8:
        for c in range(4, 8):
            if not placa[c].isnumeric():
                print('FAILURE')
                fora_padrao = True
                break
        if not fora_padrao:
            for d in range(3):
                if not placa[d].isalpha():
                    print('FAILURE')
                    fora_padrao = True
                    break

        if not fora_padrao:
            if placa[3] != '-':
                print('FAILURE')
                fora_padrao = True
                continue

    if not fora_padrao:
        if placa[7] == '1' or placa[7] == '2':
            print('MONDAY')
        elif placa[7] == '3' or placa[7] == '4':
            print('TUESDAY')
        elif placa[7] == '5' or placa[7] == '6':
            print('WEDNESDAY')
        elif placa[7] == '7' or placa[7] == '8':
            print('THURSDAY')
        elif placa[7] == '9' or placa[7] == '0':
            print('FRIDAY')
