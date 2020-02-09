products_list = {
    1001:1.5,
    1002:2.5,
    1003:3.5,
    1004:4.5,
    1005:5.5
}

p = int(input())
sum = 0

if(1 <= p <=5):
    for i in range(p):
        q,times = list(map(int,input().split(" ")))
        sum+=(products_list[q]*times)
    print("{:.2f}".format(sum))