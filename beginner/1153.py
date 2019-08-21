N = int(input())

if(0<N<13):
    fatorial = 1
    for i in range(N):
        fatorial *= (N-i)
    print(fatorial)