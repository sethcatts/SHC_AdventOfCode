import os 

input = open("input.txt", "r")
lines = input.readlines()

# Read each line
# get the first and last integer from each line
# concat and add to the total
a = "0"
b = "0"
total = 0
firstInt = True

for lineNumber in range(0, len(lines)):

    #Ugly but it works!
    og = lines[lineNumber]
    lines[lineNumber] = str(lines[lineNumber]).replace("one", "one1one")
    lines[lineNumber] = str(lines[lineNumber]).replace("two", "two2two")
    lines[lineNumber] = str(lines[lineNumber]).replace("three", "three3three")
    lines[lineNumber] = str(lines[lineNumber]).replace("four", "four4four")
    lines[lineNumber] = str(lines[lineNumber]).replace("five", "five5five")
    lines[lineNumber] = str(lines[lineNumber]).replace("six", "six6six")
    lines[lineNumber] = str(lines[lineNumber]).replace("seven", "seven7seven")
    lines[lineNumber] = str(lines[lineNumber]).replace("eight", "eight8eight")
    lines[lineNumber] = str(lines[lineNumber]).replace("nine", "nine9nine")
    print("{} → {}".format(og, lines[lineNumber]))


    #Look at all the characters in the line 
    for char in lines[lineNumber]:
        if(char.isnumeric() and firstInt):
            a = char
            b = char
            firstInt = False
        elif(char.isnumeric()):
            b = char
    addition = int(str(a) + str(b))
    total += addition
    print("A = {}, B = {} | New Total: {}\n\n".format(a, b, total))
    firstInt = True

print("The total is: {}".format(total))
# Correct answer (p1): 54561
# Incorrect answer (p2): 53616
# Correct answer (p2): 54076