case_tests = int(input())

for i in range(case_tests):
    challenger = input().split(" ")
    if challenger[0] == "Thor":
        print("Y")
    else:
        print("N")
    challenger.clear()