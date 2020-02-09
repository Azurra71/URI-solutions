def line(i):
    char = "-"
    l = ""
    for index in range(i):
        l+=char
    print(l)

def bars(i):
    bars = "|                                     |"
    for index in range(i):
        print(bars)    

line(39)
bars(5)
line(39)