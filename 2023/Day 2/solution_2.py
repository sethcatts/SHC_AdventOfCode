import os 

input = open("input.txt", "r")
lines = input.readlines()

class gameParser:
    def __init__(self, line):
            self.gameID = line.split(":")[0].split(" ")[1]   
            self.rounds = line[int(line.index(":"))+1:len(line)].split(";") 
            for i in range(0, len(self.rounds)):
                  self.rounds[i] = self.rounds[i].split(",")
total = 0
# For every game
for game in lines:
    # Create a game parse object
    gameData = gameParser(game)
    maxGreen = 0
    maxRed   = 0
    maxBlue  = 0

    # Check all the rounds of that game
    for i in range(0, len(gameData.rounds)):

        # Check all the color pulls from that round
        for j in range(0, len(gameData.rounds[i])):

            # Get the color and number of that color pulled
            num = gameData.rounds[i][j].strip().split(" ")[0]
            color = gameData.rounds[i][j].strip().split(" ")[1]
            #rint("{} - {}".format(num, color))

            if(color == "green" and int(num) > maxGreen):
                maxGreen = int(num)
            elif(color == "red" and int(num) > maxRed):
                maxRed = int(num)
            elif(color == "blue" and int(num) > maxBlue):
                maxBlue = int(num)
    total += maxRed * maxBlue * maxGreen
     
print("Total: {}".format(total))

# Incorrect answer (p1): 286 <
# Correct answer (p1): 2810





