T = int(input())

if(2 <= T <= 50):
    N = []
    count = 0

    for index in range(1000):
        if(count % T == 0):
            count = 0
        N.append(count)
        count+=1
        print("N[{}] = {}".format(index,N[index]))