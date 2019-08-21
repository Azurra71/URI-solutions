def primo(number:int):
    div_list = []
    for i in range(1,number+1):
        if(number%i == 0):
            div_list.append(int(i))
    if len(div_list) > 2:
        print("{} nao eh primo".format(number))
    else:
        print("{} eh primo".format(number))

N = int(input())
if(1 <= N <= 100):
    for i in range(N):
        X = int(input())
        if(1 < X <= pow(10,7)):
            primo(X)
