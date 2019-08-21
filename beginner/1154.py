idade = int(input())
i = 0
acumulo = 0
while(idade >= 0):
    acumulo+=idade
    i+=1
    idade = int(input())
print("{:.2f}".format(acumulo/i))