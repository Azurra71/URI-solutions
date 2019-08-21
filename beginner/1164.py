def perfect(number:int):
    div_list = []
    condition = 0
    for i in range(1,number):
        if(number%i==0):
            div_list.append(int(i))
    for div in div_list:
        condition+=div
    if(number == condition):
        print("{} eh perfeito".format(number))
    else:
        print("{} nao eh perfeito".format(number))

N = int(input())
if(1<=N<=20):
    for i in range(N):
        X = int(input())
        if(1<=X<=pow(10,8)):
            perfect(X)