input = open("input.txt", "r")
lines = input.readlines()

total = 0

for line in lines:
    paper = 0
    d = line.strip().split("x")
    dx = [eval(i) for i in d]
    dx.sort()
    paper += dx[0]
    paper += (2 * dx[0]) + (2 * dx[1]) + (2 * dx[2])
    print(dx)
    print("2 * {} + 2 * {} + 2 * {} + {}".format(dx[0], dx[1], dx[2], dx[0]))
    total += paper

print("Total paper needed {} sqft".format(total))

# Missing side area code LxWxH


# Wrong answer: 101578 <