a,b,c = input().split(" ")

pi = 3.14159
a = float(a)
b = float(b)
c = float(c)

triangle = 0.5 * a * c
circle = pi * pow(c,2)
trapezium = a*c/2 + b*c/2
square = b * b
rectangle = a * b

print("TRIANGULO: {:.3f}".format(triangle))
print("CIRCULO: {:.3f}".format(circle))
print("TRAPEZIO: {:.3f}".format(trapezium))
print("QUADRADO: {:.3f}".format(square))
print("RETANGULO: {:.3f}".format(rectangle))