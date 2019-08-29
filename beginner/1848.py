def crow_to_decimal(blinks:str) -> int:
    #--* *-- -*-
    blink_dict = {"-":"0","*":"1"}
    blink_string = blink_dict[blinks[0]]+blink_dict[blinks[1]]+blink_dict[blinks[2]]
    return int(blink_string,2)

caw_counter = 0
lottery = 0
while(caw_counter < 3):
    crow_input = input()

    if(crow_input != "caw caw"):
        lottery+=crow_to_decimal(crow_input)
    else:
        print(lottery)
        caw_counter+=1
        lottery = 0