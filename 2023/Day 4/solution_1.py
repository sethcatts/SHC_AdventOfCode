input = open("input.txt", "r")
lines = input.readlines()
total = 0

card1 = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
card2 = "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19"
card3 = "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1"
card4 = "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83"
card5 = "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36"
card6 = "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"

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


# print("Value of test card: {}".format(getCardValue(card1)))
# print("Value of test card: {}".format(getCardValue(card2)))
# print("Value of test card: {}".format(getCardValue(card3)))
# print("Value of test card: {}".format(getCardValue(card4)))
# print("Value of test card: {}".format(getCardValue(card5)))
# print("Value of test card: {}".format(getCardValue(card6)))

for line in lines:
    total += getCardValue(line)
print("Total: {}".format(total))

#Incorrect answer (p1): 14773 <
#Correct answer (p1): 17782
