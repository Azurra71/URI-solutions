rounds = int(input())

for i in range(rounds):
    duel = input().split(" ")
    outcome = {1:"Bazinga!",2:"Raj trapaceou!",3:"De novo!"}
    result = 0

    if(duel[0] != duel[1]):
        if(duel[0] == "tesoura"):
            if(duel[1] == "lagarto" or duel[1] == "papel"):result = 1 
            else:result = 2
        
        if(duel[0] == "papel"):
            if(duel[1] == "pedra" or duel[1] == "Spock"):result = 1 
            else:result = 2

        if(duel[0] == "pedra"):
            if(duel[1] == "lagarto" or duel[1] == "tesoura"):result = 1 
            else:result = 2

        if(duel[0] == "lagarto"):
            if(duel[1] == "Spock" or duel[1] == "papel"):result = 1 
            else:result = 2
        
        if(duel[0] == "Spock"):
            if(duel[1] == "tesoura" or duel[1] == "pedra"):result = 1 
            else:result = 2
    else: result = 3

    print("Caso #{}: {}".format(i+1,outcome[result]))