N = int(input())
ho_string = ""

if(0 <= N <= pow(10,6)):
    for i in range(N):
        ho_string+="Ho "
    ho_string = ho_string[:-1]+"!"
    print(ho_string)