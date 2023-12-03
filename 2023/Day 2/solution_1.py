import os 

input = open("input.txt", "r")
lines = input.readlines()

class game:
    def __init__(self, line):
            # Ex: 12
            self.gameID = line.split(":")[0].split(" ")[1]   
                          
            # Ex: [[' 10 blue', ' 6 green', ' 5 red'], [' 2 red', ' 2 green'], [' 8 blue', ' 5 red'], 
            #      [' 7 blue', ' 11 green'], [' 8 green', ' 9 blue\n']]
            self.rounds = line[int(line.index(":"))+1:len(line)].split(";") 
            for i in range(0, len(self.rounds)):
                  self.rounds[i] = self.rounds[i].split(",")

#What games are possible with only 12 red, 13 green, and 14 blue cubes
#Ex. Game 9: 1 green, 5 blue; 4 blue; 2 red, 1 blue
gameData = game(lines[25])
total = 0
roundFailed = False

# Check for any failing rounds

# For every round inside the list of rounds
for i in range(0, len(gameData.rounds)):
    # For every item in the round
    for j in range(0, len(gameData.rounds[i])):
            num = gameData.rounds[i][j].strip().split(" ")[0]
            color = gameData.rounds[i][j].strip().split(" ")[1]
            if(color == "green" and int(num) > 13):
                  roundFailed = True
            elif(color == "red" and int(num) > 12):
                  roundFailed = False
            elif(color == "blue" and int(num) > 14):
                  roundFailed = False      
            else:
                  total += int(gameData.gameID)

print(total)

# Incorrect answer (p1): 286 <
# Incorrect answer (p1): 



