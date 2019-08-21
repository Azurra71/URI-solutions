salary = float(input())

if (0 < salary <= 400):
    readjust_rate = 0.15
elif (400 < salary <= 800):
    readjust_rate = 0.12
elif (800 < salary <= 1200):
    readjust_rate = 0.10
elif (1200 < salary <= 2000):
    readjust_rate = 0.07
else:
    readjust_rate = 0.04

readjust = readjust_rate * salary
salary = salary  + readjust

print("Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: {:.0f} %".format(salary,readjust,readjust_rate*100))