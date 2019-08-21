import math

numbers = input().split(" ")
numbers = list(map(float,numbers))

a = numbers[0]
b = numbers[1]
c = numbers[2]
delta = pow(b,2) - 4*a*c

if(delta < 0 or a == 0):
    print("Impossivel calcular")
else:
    r1,r2 = (-b + math.sqrt(delta))/(2*a),(-b - math.sqrt(delta))/(2*a)
    print("R1 = {:.5f}".format(r1))
    print("R2 = {:.5f}".format(r2))