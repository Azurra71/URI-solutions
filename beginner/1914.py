QT = int(input())
if(1 <= QT <= 100):
    for i in range(QT):
        players = []
        choices = []
        game_string = input().split(" ")
        duel = list(map(int,input().split(" ")))

        for j in range(len(game_string)):
            if(j%2 != 0): choices.append(game_string[j])
            else: players.append(game_string[j])
        
        result = duel[0] + duel[1]
        if(choices[0] == "PAR"):
            if(result%2 == 0): print(players[0])
            else: print(players[1])

        if(choices[0] == "IMPAR"):
            if(result%2 != 0): print(players[0])
            else: print(players[1])