size = int(input())

numbers = list(map(int,input().split(" ")))

print("Menor valor: {}".format(min(numbers)))
print("Posicao: {}".format(numbers.index(min(numbers))))