exe = input().split()
bem = int(exe[0]) + int(exe[1]) + int(exe[2]) + int(exe[5])
mal = int(exe[3]) + int(exe[4])
if bem > mal:
    print('Middle-earth is safe.')
else:
    print('Sauron has returned.')
