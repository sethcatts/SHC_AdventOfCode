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

#Look at all lines
for line in lines:
    #Look at all the characters in the line 
    for char in line:
        if(char.isnumeric() and firstInt):
            a = char
            b = char
            firstInt = False
        elif(char.isnumeric()):
            b = char
    addition = int(str(a) + str(b))
    total += addition
    firstInt = True

print("The total is: {}".format(total))
# Correct answer: 54561