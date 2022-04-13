time = int(input())
hours = minutes = seconds = 0
if time >= 3600:
    hours = time // 3600
    time = time - (hours * 3600)
if time >= 60:
    minutes = time // 60
    time = time - (minutes * 60)
seconds = time
print(f'{hours}:{minutes}:{seconds}')
