import math

while True:
    try:
        V = float(input())
        D = float(input())
        pi = 3.14
        a = (pi * pow((0.5 * D),2))
        h = V/a
        
        print("ALTURA = {:.2f}".format(h))
        print("AREA = {:.2f}".format(a))
    except EOFError:
        break