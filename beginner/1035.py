numbers = input().split(" ")
numbers = list(map(int,numbers))

#if B is greater than C and D is greater than A and 
#if the sum of C and D is greater than the sum of A and B and 
#if C and D were positives values and 
#if A is even

if(numbers[0]%2 == 0 and numbers[2] > 0 and numbers[3] > 0 and 
numbers[2]+numbers[3] > numbers[0]+numbers[1] and 
numbers[1] > numbers[2] and numbers[3] > numbers[0]):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")