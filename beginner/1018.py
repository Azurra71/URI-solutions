def decompose(n) -> list:
    bills = [100,50,20,10,5,2,1]
    change = []
    for bill in bills:
        change.append(n//bill)
        n = n - (n//bill)*bill
    return change,bills

n = int(input())
if (0 < n and n < 1000000):
    change,bills = decompose(n)
    index = 0
    print(n)
    for i in change:
        print("{} nota(s) de R$ {},00".format(i,bills[index]))
        index+=1