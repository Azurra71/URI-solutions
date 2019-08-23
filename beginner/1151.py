def fibonacci(number:int) -> list:
    fibo_list = []
    for i in range(number):
        if(i == 0 or i == 1):
            fibo_list.append(i)
        else:
            fibo_list.append(fibo_list[i-2]+fibo_list[i-1])
    return fibo_list

N = int(input())
if(0 < N < 46):
    answer_string = ' '.join(str(number) for number in fibonacci(N))
    print(answer_string)
