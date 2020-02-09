C = int(input())

for i in range(C):
    values = list(map(int,input().split(" ")))
    result = pow(values[0],values[1])
    result = str(result)

    print(len(result))
