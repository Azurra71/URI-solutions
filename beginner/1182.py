def create_matrice(collums:int,rows:int,data:list) -> list:
    matrice = []
    for i in range(collums):
        row_list = []
        for j in range(rows):
            row_list.append(data[rows* i + j])
        matrice.append(row_list)
    return matrice

C = int(input())
T = input()
sum = 0
data = []
i = 0
for i in range(144):
    number = float(input())
    data.append(number)

matrice = create_matrice(12,12,data)
if(0 <= C <= 11):
    for i in range(len(matrice)):
        sum+=matrice[i][C]

    if(T == 'S'):
        print("{:.1f}".format(sum))
    elif(T == 'M'):
        avg=sum/12
        print("{:.1f}".format(avg))