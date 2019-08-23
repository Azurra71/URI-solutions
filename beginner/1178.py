X = float(input())
N = []

for index in range(100):
    N.append(X)
    print("N[{}] = {:.4f}".format(index,N[index]))
    X*=0.5