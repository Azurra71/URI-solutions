a,b = list(map(int,input().split(" ")))

if (a in range(-1000,1001) and b in range(-1000,1001)):
    if(b != 0):

        if(a != 0):
            if(b>0): r = a%b
            if(b<0): r = a%-b
            q = (a - (r))//b
        else:
            q = 0
            r = 0
        
        print("{} {}".format(q,r))