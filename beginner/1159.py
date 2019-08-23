X = int(input())

while(X != 0):
    sum = 0
    if(X%2 == 0):
        next_even=X
    else:
        next_even=X+1

    for i in range(5):
        sum+=next_even
        next_even+=2
        
    print(sum)
    X = int(input())