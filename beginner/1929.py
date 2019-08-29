def possible_triangle(a:int, b:int, c:int) ->  bool:
    if(abs(b - c) < a < (b + c)):
        if(abs(a - c) < b < (a + c)):
            if(abs(a - b) < c <(a + b)):
                return True
    else:
        return False

a,b,c,d = list(map(int,input().split(" ")))

if(1 <= a,b,c,d <= 100):
    if(possible_triangle(a,b,c) or possible_triangle(a,b,d) or 
    possible_triangle(b,c,d) or possible_triangle(a,c,d)):
        print("S")
    else:
        print("N")