def line(i:int):
    char = "-"
    l = ""
    for index in range(i):
        l+=char
    print(l)

def bars():
    bars = "|x = 35                               |"
    print(bars)
    bars = "|                                     |"
    print(bars)
    bars = "|               x = 35                |"
    print(bars)
    bars = "|                                     |"
    print(bars)
    bars = "|                               x = 35|"
    print(bars)    

line(39)
bars()
line(39)