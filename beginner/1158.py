case_tests = int(input())

for i  in range(case_tests):
    X,Y = map(int,(input().split(" ")))
    sum = 0
    if(X%2 == 0):
        next_odd=X+1
    else:
        next_odd=X

    for i in range(Y):
        sum+=next_odd
        next_odd+=2
        
    print(sum)