X = int(input())
Z = int(input())

if(Z <= X):
    while(Z <= X):
        Z=int(input())

i=1
result = X
while(result<=Z):
    result+=X+i
    i+=1

print(i)