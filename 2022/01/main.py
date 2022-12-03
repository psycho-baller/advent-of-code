f = open("input.txt", "r")
currMax = 0
currSum = 0

for v in f:
    v = v.strip("\n")

    if v != "\n" and v != "":
        currSum+=int(v)
    else:
        currMax = max(currMax, currSum)
        currSum = 0
print(currMax)
