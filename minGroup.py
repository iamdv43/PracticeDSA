def minGroup(awards, k):
    awards.sort()
    g = 1
    index = 0
    for j in range(index+1, len(awards)):
        if awards[j] - awards[index] > k:
            index = j
            g += 1
    return g

awards = [1,5,4,6,8,9,2]
k = 3
print("Number of groups: ", minGroup(awards, k))

awards = [100,11,122,25,19, 125]
k = 25
print("Number of groups: ", minGroup(awards, k))