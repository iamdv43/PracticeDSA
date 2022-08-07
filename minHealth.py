def findMinHealth (power, armor):
    return sum(power) - armor + 1

power = [1,2,6,7]
armor = 5
print("Min Health: ", findMinHealth(power, armor))