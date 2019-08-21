day_i = input().split(" ")
day_i = int(day_i[1])
start = list(map(int,input().split(":")))

day_f = input().split(" ")
day_f = int(day_f[1])
finish = list(map(int,input().split(":")))

current_time = [day_i,start[0],start[1],start[2]]
goal_time = [day_f,finish[0],finish[1],finish[2]]
dd = 0
hh = 0
mm = 0
ss = 0

while(current_time != goal_time):
    
    current_time[3]+=1
    ss+=1

    if(ss==60):
        mm+=1
        ss=ss%60
    if(current_time[3] == 60):
        current_time[3] = 0
        current_time[2]+=1
        
    if(mm==60):
        mm=mm%60 
        hh+=1    
    if(current_time[2] == 60):
        current_time[2] = 0
        current_time[1]+=1

    if(hh==24):
        hh=hh%24
        dd+=1
    if(current_time[1] == 24):
        current_time[1] = 0
        current_time[0]+=1
    
print("{} dia(s)".format(dd))
print("{} hora(s)".format(hh))
print("{} minuto(s)".format(mm))
print("{} segundo(s)".format(ss))

#Time exceed, cool code but not efficient