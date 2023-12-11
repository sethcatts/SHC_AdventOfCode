input = open("input.txt", "r")
lines = input.readlines()

total = 0

for line in lines:
    paper = 0
    d = line.strip().split("x")
    dx = [eval(i) for i in d]
    l = dx[0]
    w = dx[1]
    h = dx[2]
    dx.sort()
    print("L {} W {} H {} S {}".format(l, w, h, dx[0]))
    #print("{} {} {} {}".format((2 * l * w), (2 * w * h), (2 * h * l), dx[0]))
    print("{}".format((2 * l * w) + (2 * w * h) + (2 * h * l) + dx[0]))
    total += (2 * l * w) + (2 * w * h) + (2 * h * l) + dx[0]

print("Total paper needed {} sqft".format(total))

# Missing side area code LxWxH
# Wrong answer: 101578 <
# Wrong answer: 1464826 <