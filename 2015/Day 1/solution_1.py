input = open("input.txt", "r")
lines = input.readlines()[0]

floor = 0
print(lines[2])
for i in lines:
    if(i == "("):
        floor += 1
    else:
        floor -= 1

print("Floor: {}".format(floor))


# Wrong answers: -232
# Correct answer: 232
