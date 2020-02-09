def line(i:int):
    char = "-"
    l = ""
    for index in range(i):
        l+=char
    print(l)

dec_list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
octal_list = [0,1,2,3,4,5,6,7,10,11,12,13,14,15,16,17]
hex_list = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]

line(39)
print("|  decimal  |  octal  |  Hexadecimal  |")
line(39)
for i in range(8):
    print("|      {}    |    {}    |       {}       |".format(dec_list[i],octal_list[i],hex_list[i]))
for i in range(8,10):
    print("|      {}    |   {}    |       {}       |".format(dec_list[i],octal_list[i],hex_list[i]))
for i in range(10,16):
    print("|     {}    |   {}    |       {}       |".format(dec_list[i],octal_list[i],hex_list[i]))
line(39)