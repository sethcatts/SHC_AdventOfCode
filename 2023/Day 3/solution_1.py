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
    
# Do the stuff