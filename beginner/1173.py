import array as arr

V = int(input())
N = arr.array('i')

if(V <= 50):
    N.append(V)
    for i in range(1,10):
        V*=2
        N.append(V)
        
    for index in range(len(N)):
        print("N[{}] = {}".format(index,N[index]))