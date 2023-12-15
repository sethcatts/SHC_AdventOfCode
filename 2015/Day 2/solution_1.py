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

    areaList = []
    areaList.append(2 * l * w)
    areaList.append(2 * w * h)
    areaList.append(2 * h * l)
    areaList.sort()

    areaLista = []
    areaLista.append(l * w)
    areaLista.append(w * h)
    areaLista.append(h * l)
    areaLista.sort()

    print("{} + {} + {} + {} = ".format(areaList[0], areaList[1], areaList[2], areaLista[0]), (areaList[0] + areaList[1] + areaList[2] + areaLista[0]))
    total += (areaList[0] + areaList[1] + areaList[2] + areaLista[0])

print("Total paper needed {} sqft".format(total))

# Wrong answer: 101578 <
# Wrong answer: 1464826 <
# Correct answer: 1606483 