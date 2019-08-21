sides = list(map(float,input().split(" ")))
sides.sort(reverse = True)

a,b,c = sides

if(a >= b+c):
    print("NAO FORMA TRIANGULO")
else:
    if (pow(a,2) == pow(b,2)+pow(c,2)):
        print("TRIANGULO RETANGULO")
    if (pow(a,2) > pow(b,2)+pow(c,2)):
        print("TRIANGULO OBTUSANGULO")
    if (pow(a,2) < pow(b,2)+pow(c,2)):
        print("TRIANGULO ACUTANGULO")
    if(a == b == c):
        print("TRIANGULO EQUILATERO")
    if( (a == b and a != c) or (a == c and a != b) or (c == b and c != a) ):
        print("TRIANGULO ISOSCELES")