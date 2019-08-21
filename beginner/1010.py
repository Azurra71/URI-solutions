#code units price

code_1, unit_1, price_1 = input().split(" ")
code_2, unit_2, price_2 = input().split(" ")

TOTAL = float(unit_1)*float(price_1) + float(unit_2)*float(price_2)

print("VALOR A PAGAR: R$ {:.2f}".format(TOTAL))