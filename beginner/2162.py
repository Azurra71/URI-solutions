N = int(input())
nlog_flag = 1

if(1 < N <= 100):
    pattern = list(map(int,input().split(" ")))
    
    if(len(pattern) == 2 and (pattern[0] == pattern[1])):
        nlog_flag = 0

    if(len(pattern) > 2):
        for index in range(2,len(pattern)):
            if(pattern[index] >= pattern[index-1] and pattern[index-1] >= pattern[index-2]):
                nlog_flag = 0
                break
            elif(pattern[index] <= pattern[index-1] and pattern[index-1] <= pattern[index-2]):
                nlog_flag = 0
                break
    
    print(nlog_flag)