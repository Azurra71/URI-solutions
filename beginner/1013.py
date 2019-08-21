a,b,c = input().split(" ")

a = int(a)
b = int(b)
c = int(c)

def MaiorAB(a,b) -> int:
    maior = (a+b+abs(a-b))*0.5
    return maior

temp = MaiorAB(a,b)
maior_real = MaiorAB(temp,c)

print("{:.0f} eh o maior".format(maior_real))