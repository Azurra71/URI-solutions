N = []
for i in range(20):
    N.append(int(input()))


for index in range(10):
    temp1 = N[19-index]
    temp2 = N[index]

    N[index] = temp1
    N[19-index] = temp2
   
for index in range(len(N)):
    print("N[{}] = {}".format(index,N[index]))