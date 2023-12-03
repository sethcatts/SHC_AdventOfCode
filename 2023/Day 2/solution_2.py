import os 

input = open("input.txt", "r")
lines = input.readlines()

class gameParser:
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
total = 0
roundFailed = False

# For every game
for game in lines:
      # Create a game parse object
      gameData = gameParser(game)

      # Check all the rounds of that game
      for i in range(0, len(gameData.rounds)):

            # Check all the color pulls from that round
            for j in range(0, len(gameData.rounds[i])):

                  # Get the color and number of that color pulled
                  num = gameData.rounds[i][j].strip().split(" ")[0]
                  color = gameData.rounds[i][j].strip().split(" ")[1]
                  print("{} - {}".format(num, color))

                  # Set round pass to false if the number of pulled cubes is not allowed
                  if(color == "green" and int(num) > 13):
                        print("failed green")
                        roundFailed = True
                  elif(color == "red" and int(num) > 12):
                        print("failed red")
                        roundFailed = True
                  elif(color == "blue" and int(num) > 14):
                        print("failed blue\n\n")
                        roundFailed = True      

      if(roundFailed is False):
            print(gameData.gameID)
            total += int(gameData.gameID)
      roundFailed = False

print("Total: {}".format(total))

# Incorrect answer (p1): 286 <
# Correct answer (p1): 2810



