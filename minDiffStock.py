def findEarliestMonth(stockPrice):
    n = len(stockPrice)
    minD = max(stockPrice)
    for i in range(1,n):
        avg1 = sum(stockPrice[:i]) // i
        avg2 = sum(stockPrice[i:]) // (n-i)
        if minD > abs(avg2 - avg1):
            minD = abs(avg2 - avg1)
            earliestMonth = i
    return earliestMonth

stockPrice = [1,3,2,3]
print("1 Min diff: ", findEarliestMonth(stockPrice))

stockPrice = [1,3,2,4,5]
print("2 Min diff: ", findEarliestMonth(stockPrice))

stockPrice = [1,1,1,1,1,1]
print("3 Min diff: ", findEarliestMonth(stockPrice))