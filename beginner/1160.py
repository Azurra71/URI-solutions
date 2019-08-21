import math

def outgrow_time(popA:int,popB:int,gA:float,gB:float)->int:
    years=0
    while(popA <= popB):
        popA+=math.trunc(popA*(gA/100))
        popB+=math.trunc(popB*(gB/100))
        years+=1
        if(years%101==0):
            break
    return years


T = int(input())

if(1 <= T <= 3000):
    for i in range(T):
        PA,PB,G1,G2 = list(map(float,input().split(" ")))
        PA=int(PA)
        PB=int(PB)
        years = outgrow_time(PA,PB,G1,G2)
        if(years<=100):
            print("{} anos.".format(years))
        else:
            print("Mais de 1 seculo.")