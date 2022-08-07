def minCost(parcels, k):
    rem = sorted(set(range(1, k + 1)) - set(parcels))
    cost = 0
    for i in range(k - len(parcels) - 1):
        cost += rem[i]
    return cost

parcels = [2,3,6,10,11]
k=25
print("Min cost: ", minCost(parcels, k))