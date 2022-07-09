from math import floor

for c in range(int(input())):
    abdg = input()
    r,g,b = map(int, input().split())
    if abdg == "min":
        print(f'Caso #{c + 1}:', min([r,g,b]))
    elif abdg == "max":
        print(f'Caso #{c + 1}:', max([r,g,b]))
    elif abdg == "mean":
        r = (r + g + b) / 3
        print(f'Caso #{c + 1}:', floor(r))
    elif abdg == "eye":
        r = ((0.3 * r) + (0.59 * g) + (0.11 * b))
        print(f'Caso #{c + 1}:', floor(r))
