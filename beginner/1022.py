from fractions import Fraction

#funçao para criar listas de fraçoes (Numerador,Denominador) e operaçoes
def create_frac_list(l:list) -> list:
    frac_list = [] # fraçoes
    op = [] # operação
    for i in range(len(l)):
        frac_list.append( (int(l[i][0]),int(l[i][2])) )
        frac_list.append( (int(l[i][4]),int(l[i][6])) )
        op.append(l[i][3])
    return frac_list,op

#funçao para calcular sem simplificar
def rational_calc(frac_list:list,op:list) -> list:
    i = 0
    new_frac_list = []
    for op_index in range(len(op)):
        if op[op_index] == "+":
            N = (frac_list[i][0]*frac_list[i+1][1] + frac_list[i+1][0]*frac_list[i][1])
            D = (frac_list[i][1]*frac_list[i+1][1])
            new_frac_list.append((N,D))
            i+=2           

        elif op[op_index] == "-":
            N = (frac_list[i][0]*frac_list[i+1][1] - frac_list[i+1][0]*frac_list[i][1])
            D = (frac_list[i][1]*frac_list[i+1][1])
            new_frac_list.append((N,D))
            i+=2
                        
        elif op[op_index] == "*":
            N = (frac_list[i][0]*frac_list[i+1][0])
            D = (frac_list[i][1]*frac_list[i+1][1])
            new_frac_list.append((N,D))
            i+=2

        elif op[op_index] == "/":
            N = (frac_list[i][0]*frac_list[i+1][1])
            D = (frac_list[i+1][0]*frac_list[i][1])
            new_frac_list.append((N,D))
            i+=2

    return new_frac_list


case_tests = [] # lista para guardar casos de teste
N = int(input())

if(1 <= N and N <= 10000):
    for i in range(N):
        case_tests.append(input().split(" "))

fractions,op = create_frac_list(case_tests)
results = rational_calc(fractions,op)

for i in range(N):
    frac = Fraction(results[i][0],results[i][1])
    print("{}/{} = {}/{}".format(results[i][0],results[i][1],frac._numerator,frac._denominator))