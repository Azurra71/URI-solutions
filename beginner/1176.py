def fibonacci(number:int) -> list:
    fibo_list = []
    if(number == 0):
        fibo_list.append(0)
        return fibo_list
    for i in range(number+1):
        if(i == 0 or i == 1):
            fibo_list.append(i)
        else:
            fibo_list.append(fibo_list[i-2]+fibo_list[i-1])
    return fibo_list

case_tests = int(input())

for i in range(case_tests):
    N = int(input())
    if(0 <= N <= 60):
        fibo_list = fibonacci(N)
        print("Fib({}) = {}".format(N,fibo_list[N]))