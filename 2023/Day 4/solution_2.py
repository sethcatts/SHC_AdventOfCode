input = open("testdata.txt", "r")
lines = input.readlines()
total = 0

# Loop through all the cards
# For each winning number on any card
# gain copies of scratch cards further down the list equal to the number of winning numbers
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
    print("Winning numbers: {}\nCard numbers: {}\nValue: {}".format(winningNumbers, cardNumbers, value))
    return value


for line in lines:
    total += getCardValue(line)
print("Total: {}".format(total))


