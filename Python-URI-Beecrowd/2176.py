m = input()
if m.count('1') % 2 != 0:
    m = list(m)
    m.append('1')
    m = ''.join(m)
    print(m)
else:
    m = list(m)
    m.append('0')
    m = ''.join(m)
    print(m)
