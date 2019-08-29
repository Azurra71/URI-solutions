'''
A A A >>> A A 3
13 13 13 >>> 12 12 12
3 3 A >>> 2 2 A
'''
a,b = list(map(int,input().split(" ")))

if(1 <= a,b <= 13):
    if (a == b):
        print(a)
    else:
        if(a > b):print(a)
        else: print(b)