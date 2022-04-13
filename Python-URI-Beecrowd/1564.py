copa = True
while copa:
    try:
        rec = int(input())
        if rec == 0:
            print('vai ter copa!')
        else:
            print('vai ter duas!')
    except EOFError:
        copa = False
