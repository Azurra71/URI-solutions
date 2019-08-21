duration = int(input())

def decompose(n):
    timescales = [3600,60,1]
    timestamp = []
    for i in timescales:
        if(n < i):
            timestamp.append(0)
            n = n - (n//i)*i
        else:
            timestamp.append(n//i)
            n = n - (n//i)*i
    return timestamp

timestamp = decompose(duration)
print("{}:{}:{}".format(timestamp[0],timestamp[1],timestamp[2]))