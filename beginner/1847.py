while True:
    try:
        a,b,c = list(map(int,input().split(" ")))

        if(-100 <= a,b,c <= 100):

            delta_ab = b - a
            delta_bc = c - b

            if(delta_ab == 0):
                if(delta_bc > 0): print(":)")
                else: print(":(")

            else:
                if(delta_ab < 0):
                    if(delta_bc < 0):
                        if(delta_bc > delta_ab): print(":)")
                        else:  print(":(")
                    else: print(":)")

                else:
                    if(delta_bc > 0):
                        if(delta_bc >= delta_ab): print(":)")
                        else: print(":(")
                    else: print(":(")
    except EOFError:
        break