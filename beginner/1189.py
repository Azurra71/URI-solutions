def create_matrice(collums:int,rows:int,data:list) -> list:
    matrice = []
    for i in range(collums):
        row_list = []
        for j in range(rows):
            row_list.append(data[rows* i + j])
        matrice.append(row_list)
    return matrice

O = input()
sum = 0
data = []


for i in range(144):
    number = float(input())
    data.append(number)

matrice = create_matrice(12,12,data)
elements = 0
for i in range(len(matrice)):
    for j in range(len(matrice)):
        if(i + j != len(matrice)-1 and i != j):
            if(i > j and i + j < len(matrice)-1):
                elements+=1
                sum+=matrice[i][j]

if(O == 'S'):
    print("{:.1f}".format(sum))
elif(O == 'M'):
    avg=sum/elements
    print("{:.1f}".format(avg))
