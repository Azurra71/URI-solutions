T = int(input())

if(0 <= T <= 10000):
    for i in range(T):
        R1,R2 = list(map(int,input().split(" ")))
        print(R1+R2)