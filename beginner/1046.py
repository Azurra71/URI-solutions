start,finish = list(map(int,input().split(" ")))
i = 0
if(start == finish):
    i = 24
else:
    while (start != finish):
        start+=1
        start = start%24
        i+=1
print("O JOGO DUROU {} HORA(S)".format(i))