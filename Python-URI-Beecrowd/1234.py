while True:
    try:
        frase_nova = ''
        frase = input()
        maiusc = True
        for c in frase:
            if c == ' ':
                frase_nova += ' '
            elif maiusc:
                frase_nova += c.upper()
                maiusc = False
            elif maiusc == False:
                frase_nova += c.lower()
                maiusc = True
        print(frase_nova)
    except EOFError:
        break
