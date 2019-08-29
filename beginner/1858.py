N = int(input())
T = list(map(int,input().split(" ")))

def check(T:list) -> bool:
    for i in T:
        if (i > 20 or i < 0): return False
    return True

if(1 <= N <= 100 and check(T)):
    print(T.index(min(T))+1)