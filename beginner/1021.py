import math
def decompose(n) -> list:
    bills = [100,50,20,10,5,2]
    coins = [1,0.5,0.25,0.10,0.5,0.01]
    change_bills = []
    change_coins = [0.0]
    n_frac, n_whole = math.modf(n)  

    #check if is odd number, since there is no 1 real bill but 1 real coin
    if (n_whole%2 == 0):
        change_coins.append(0.0)
    elif(n_whole%2 == 1):
        change_coins.append(1.0)


    for bill in bills:
        change_bills.append(n_whole//bill)
        n_whole = n_whole - (n_whole//bill)*bill
    for coin in coins:
        change_coins.append(n_frac//coin)
        n_frac = n_frac - (n_frac//coin)*coin
    return change_bills,bills,change_coins,coins



n = float(576.73)
if (0 < n and n < 1000000):
    change_bills,bills,change_coins,coins = decompose(n)

    index = 0
    print("NOTAS:")
    for i in change_bills:
        print("{} nota(s) de R$ {}".format(i,bills[index]))
        index+=1

    index = 0
    print("MOEDAS:")
    for j in change_coins:
        print(j)
        #print("{} moeda(s) de R$ {}".format(j,coins[3]))
        index+=1      