a,b,c = list(map(float,input().split(" ")))

if(a+b > c and a+c > b and b+c > a):
    perimetro = a+b+c
    print("Perimetro = {:.1f}".format(perimetro))
else:
    area = c*(a+b)*0.5
    print("Area = {:.1f}".format(area))