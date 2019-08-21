p1 = input().split(" ")
p2 = input().split(" ")
p1 = list(map(float,p1))
p2 = list(map(float,p2))

dist = pow(pow(p2[0] - p1[0],2) + pow(p1[1] - p2[1],2),0.5)

print("{:.4f}".format(dist))