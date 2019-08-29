T = int(input())
answers = list(map(int,input().split(" ")))
correct = 0

for answer in answers:
    if(T == answer): correct+=1
        
print(correct)