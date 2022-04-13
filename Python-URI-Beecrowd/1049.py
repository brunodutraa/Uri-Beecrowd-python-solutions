in1 = input()
if in1 == 'vertebrado':
    vert = input()
    if vert == 'ave':
        ave = input()
        if ave == 'carnivoro':
            print('aguia')
        else:
            print('pomba')
    elif vert == 'mamifero':
        mamifero = input()
        if mamifero == 'onivoro':
            print('homem')
        else:
            print('vaca')
elif in1 == 'invertebrado':
    invert = input()
    if invert == 'inseto':
        inseto = input()
        if inseto == 'hematofago':
            print('pulga')
        else:
            print('lagarta')
    elif invert == 'anelideo':
        anelideo = input()
        if anelideo == 'hematofago':
            print('sanguessuga')
        else:
            print('minhoca')
