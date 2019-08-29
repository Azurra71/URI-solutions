t1,t2,t3,t4 = list(map(int,input().split(" ")))

if(2 <= t1,t2,t3,t4 <= 6):
    outlets = t1 + t2 + t3 + t4
    connections = 3
    outlets -= connections
    print(outlets)