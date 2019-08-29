C = int(input())

for i in range(C):
    N = int(input())
    if(1 <= N <= 1000):
        if(N%2 == 0): print("0")
        else: print("1")