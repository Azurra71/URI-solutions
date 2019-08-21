N = int(input())

if(1 < N < 1000):
    for i in range(1,N+1):
        print("{} {} {}".format(i,pow(i,2),pow(i,3)))
        print("{} {} {}".format(i,pow(i,2)+1,pow(i,3)+1))