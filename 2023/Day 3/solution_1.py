input = open("input.txt", "r")
lines = input.readlines()

#TODO: Function for checking if any surrounding cells have a special character in them
#   Special characters: <ANYTHING NOT A DOT OR NUMBER>
def isSpecialChar(char):
    specialCharList = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "/", "\\", "<", ">", ",", "=", "-", "+"]
    return char in specialCharList and not char.isdigit()


#Wahhhhhhhhh ugly
def hasAdjacentSpecialChar(array, i, j):
    #Above
    try:
        if(isSpecialChar(array[i-1][j-1])):
            return True
        elif (isSpecialChar(array[i-1][j])):
            return True
        elif (isSpecialChar(array[i-1][j+1])):
            return True
        
        # Left & Right
        elif (isSpecialChar(array[i][j-1])):
            return True
        elif (isSpecialChar(array[i][j+1])):
            return True
        
        # Below
        elif (isSpecialChar(array[i+1][j-1])):
            return True
        elif (isSpecialChar(array[i+1][j])):
            return True
        elif (isSpecialChar(array[i+1][j+1])):
            return True
        else:
            return False 
    except IndexError:
        print("Index out of range")

def notValidIndex(array, i):
    if(0 < i < len(array)):
        return False
    else:
        return True

def getWholeNumber(i, line):
    startIndex = 0
    endIndex = len(line)

    # Move right and check chars at index
    # if the char is not an int or if the char is not a valid index
    # set the end index to current index - 1
    # print("Length of line {}".format(len(line)))
    for x in range(i, len(line)):
        if(notValidIndex(line, x)):
            # print("Found a bad index")
            endIndex = x
            break
        elif(not line[x].isdigit()):
            # print("Found a none index")
            endIndex = x
            break
    
    # Move left and check the chars at index
    # if the char not an int or if the char not a valid index
    # set the start index to that index + 1
    for r in reversed(range(i)):
        if(notValidIndex(line, r)):
            startIndex = r+1
            break
        elif(not line[r].isdigit()):
            startIndex = r+1
            break
    print("Returning: {} | {}".format(line[startIndex:endIndex], endIndex))
    return [line[startIndex:endIndex], endIndex]

# arr = "......01234567......89........."
# numData = getWholeNumber(7, arr)
# i = numData[1]
# print("Number is {}".format(numData[0]))

total = 0

# Do the stuff
for i in range(0, len(lines)): 
    for j in range(0, len(lines[i])):
        # print("{}".format(lines[i][j]))
        if(hasAdjacentSpecialChar(lines, i, j) and lines[i][j].isdigit()):
            print("This index matched checks for a part number\n{}{}{}\n{}[{}]{}\n{}{}{}".format(lines[i-1][j-1],lines[i-1][j],lines[i-1][j+1],
                                                                                                   lines[i][j-1],lines[i][j],lines[i][j+1],
                                                                                                   lines[i+1][j-1],lines[i+1][j],lines[i+1][j+1]))
            #Add this number and move the pointer to the char after the end of this number
            numData = getWholeNumber(i, lines[i])
            print("Found a valid number | {}".format(numData[0]))
            total += int(numData[0])
            i = numData[1]


print("Total: {}".format(total))