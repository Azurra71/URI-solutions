import re

N = int(input())
days = {"1":"MONDAY","2":"MONDAY","3":"TUESDAY","4":"TUESDAY",
        "5":"WEDNESDAY","6":"WEDNESDAY","7":"THURSDAY","8":"THURSDAY",
        "9":"FRIDAY","0":"FRIDAY"}

if(0 <= N <= 1000):
    for i in range(N):
        plate = input()
        valid_plate = re.match("[A-Z]{3}[-]{1}[0-9]{4}",plate)
        
        if(valid_plate and len(plate) == 8):
            print(days[plate[-1]])
        else:
            print("FAILURE")