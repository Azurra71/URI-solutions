def check_winner(l:list):
    max_value = max(l)
    index = l.index(max_value)

    if index == 0:
        print("S") 
    else:
        print("N") 

N = int(input())
v = []

if(2<= N <= pow(10,4)):
    for i in range(N):
        value = int(input())
        if value <= 100000:
            v.append(value)
    check_winner(v)
        

