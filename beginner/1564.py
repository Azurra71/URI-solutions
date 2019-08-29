N = int(input())

while True:
    try:
        if(0 <= N <= 100):
            if(N != 0):
                print("vai ter duas!")
            else:
                print("vai ter copa!")
            N = int(input())
    except EOFError:
        break    