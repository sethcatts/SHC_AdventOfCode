input = open("testdata.txt", "r")
lines = input.readlines()
total = 0

print(len(lines))

# Loop through all the cards
# For each winning number on any card
# copy a row further down the 
# 

def getCardValue(card):
    card = card.strip()
    value = 0
    winningNumbers = list(filter(None, card.split(":")[1].split("|")[0].split(" ")))
    cardNumbers = list(filter(None, card.split(":")[1].split("|")[1].split(" ")))

    for n in cardNumbers:
        if(n in winningNumbers):
            if(value == 0):
                value = 1
            else:
                value *= 2
    #print("Winning numbers: {}\nCard numbers: {}\nValue: {}".format(winningNumbers, cardNumbers, value))
    return value

def insertCards(array, i, value):
    i += 1
    insertIndex = i + value + 1
    newArray = lines.copy()
    print(newArray)
    for idx in range(value):
        newArray.insert(insertIndex, lines[value+idx-1])
    print("{} \n\n ↓ \n\n {}".format(lines, newArray))
    return newArray

value = getCardValue(lines[0])
total += getCardValue(lines[0])
lines = insertCards(lines, 0, value)

idx = 0
# while (idx < len(lines)):
#     value = getCardValue(lines[idx])
#     total += getCardValue(lines[idx])
#     lines = insertCards(lines, idx, value)
#     idx += 1


print(idx)

print("Total: {}".format(total))


