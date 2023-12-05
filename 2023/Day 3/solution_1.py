input = open("input.txt", "r")
lines = input.readlines()

#TODO: Function for checking if any surrounding cells have a special character in them
#   Special characters: <ANYTHING NOT A DOT OR NUMBER>
def isSpecialChar(char):
    specialCharList = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "/", "\\", "<", ">", ",", "=", "-", "+"]
    for sc in specialCharList:
        if(sc == char):
            return True
    return False

def hasAdjacentSpecialChar(array, i, j):
    #Above
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

def notValidIndex(array, i):
    if(0 < i < len(array)):
        return False
    else:
        return True

# Edge case: The number is right at the end of the line
def getWholeNumber(i, line):
    startIndex = i
    endIndex = i
    for l in reversed(range(i)):
        if(notValidIndex(line, i)):
            startIndex = 0
            break
        elif(not line[l].isdigit()):
            startIndex = l+1
            break
        print("Looked at {}".format(line[l]))
    for l in range(i, len(line)):
        if(notValidIndex(line, i)):
            endIndex = len(line)
            break
        elif(not line[l].isdigit()):
            endIndex = l
            break
        print("Looked at {}".format(line[l]))
    print("Returning: {} | {}".format(line[startIndex:endIndex], endIndex))
    return [line[startIndex:endIndex], endIndex]

arr = "...............584545456656......"
for i in range(len(arr)):
    if(arr[i].isdigit()):
            numData = getWholeNumber(i, arr[i])



total = 0

# # Do the stuff
# for i in range(0, len(lines)): 
#     for j in range(0, len(lines[i])):
#         print("{}".format(lines[i][j]))
#         if(hasAdjacentSpecialChar(lines, i, j) and lines[i][j].isdigit()):
#             #Add this number and move the pointer to the char after the end of this number
#             numData = getWholeNumber(i, lines[i])
#             print("Found a valid number | {}".format(numData[0]))
#             total += int(numData[0])
#             i = numData[1]


print("Total: {}".format(total))