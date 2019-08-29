even = []
odds = []

for i in range(15):
    number = int(input())
    if(number % 2 == 0):
        even.append(number)
    else:
        odds.append(number)

    if(len(even) == 5):
        for index in range(len(even)):
            print("par[{}] = {}".format(index,even[index]))
        even.clear()
    if(len(odds) == 5):
        for index in range(len(odds)):
            print("impar[{}] = {}".format(index,odds[index]))
        odds.clear()

for index in range(len(odds)):
    print("impar[{}] = {}".format(index,odds[index]))
for index in range(len(even)):
    print("par[{}] = {}".format(index,even[index]))