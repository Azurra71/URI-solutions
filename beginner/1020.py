def decompose(n)->list:
    calendar = [365,30,1]
    age = []
    for i in calendar:
        age.append(n//i)
        n = n - (n//i)*i
    return age

age_days = int(input())
age = decompose(age_days)
print("{} ano(s)\n{} mes(es)\n{} dia(s)".format(age[0],age[1],age[2]))