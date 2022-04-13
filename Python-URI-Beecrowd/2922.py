while True:
    try:
        salas = input().split()
        resp = int(salas[1]) - int(salas[0]) - 1
        if salas[0] == salas[1]:
            resp = 0
        if resp < 0:
            resp = resp * (-1) - 2
        print(resp)
    except EOFError:
        break
