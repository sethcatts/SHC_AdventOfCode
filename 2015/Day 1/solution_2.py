input = open("input.txt", "r")
lines = input.readlines()[0]
delta = 0
floor = 0
print(lines[2])
for i in lines:
    delta += 1
    if(i == "("):
        floor += 1
    else:
        floor -= 1
    if(floor < 0):
        break

print("Floor: {}, Delta: {}".format(floor, delta))

# Correct answer: 1783

