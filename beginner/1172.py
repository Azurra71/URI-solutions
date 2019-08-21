import array as arr

X = arr.array('i')

for i in range(10):
    number = int(input())
    X.append(number)

for index in range(len(X)):
    if(X[index] <= 0):
        X[index] = 1
    print("X[{}] = {}".format(index,X[index]))