dia1 = input().split()
tempo = input().split(':')
dia2 = input().split()
tempo2 = input().split(':')

dia1 = int(dia1[1])
dia2 = int(dia2[1])
hora1 = int(tempo[0])
hora2 = int(tempo2[0])
min1 = int(tempo[1])
min2 = int(tempo2[1])
seg1 = int(tempo[2])
seg2 = int(tempo2[2])

min_seg = 60
hora_seg = min_seg * 60
dia_seg = hora_seg * 24

seg_dia1 = seg1 + min1 * min_seg + hora1 * hora_seg + dia1 * dia_seg
seg_dia2 = seg2 + min2 * min_seg + hora2 * hora_seg + dia2 * dia_seg

tempo_sobra = seg_dia2 - seg_dia1
dias = int(tempo_sobra // dia_seg)
tempo_sobra = tempo_sobra % dia_seg
horas = int(tempo_sobra // hora_seg)
tempo_sobra = tempo_sobra % hora_seg
minutos = int(tempo_sobra // min_seg)
tempo_sobra = tempo_sobra % min_seg
segundos = tempo_sobra

print(f'{dias} dia(s)')
print(f'{horas} hora(s)')
print(f'{minutos} minuto(s)')
print(f'{segundos} segundo(s)')
