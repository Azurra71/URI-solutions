day_i = input().split()
start = list(map(int,input().split(":")))
day_f = input().split()
finish = list(map(int,input().split(":")))

di, df = int(day_i[1]), int(day_f[1])
hi, mi, si = start[0],start[1],start[2]
hf, mf, sf = finish[0],finish[1],finish[2]

i = si + mi*60 + hi*3600 + di*86400
f = sf + mf*60 + hf*3600 + df*86400

if i < f:
    duration = f - i
    days = int(duration/86400)
    duration = duration%86400
    hours = int(duration/3600)
    duration = duration%3600
    mins = int(duration/60)
    duration = duration%60
    secs = duration
    print('{} dia(s)\n{} hora(s)\n{} minuto(s)\n{} segundo(s)'.format(days, hours, mins, secs))