N = 1
D = 1
S = N/D
for i in range(20):
    S+=(N+2)/(D*2)
    N+=2
    D*=2
print("{:.2f}".format(S))