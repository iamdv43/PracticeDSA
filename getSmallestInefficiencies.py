def getSmallestInefficiencies(skills, k):
    skills.sort()
    lo = 0
    hi = max(skills)
    while (lo < hi):
        mid = (lo + hi + 1) >> 1
        cnt = 0
        j = 0
        for i in range(len(skills)):
            while skills[i] - skills[j] > mid:
                j += 1
            cnt += i - j 
        if cnt <= k:
            lo = mid
        else:
            hi = mid - 1
    ans = [None] * k
    j = 0
    for i in range(len(skills)):
        while skills[i] - skills[j] > lo:
            j += 1
        for s in range(j, i):
            k -= 1
            ans[k] = skills[i] - skills[s]
    while(k>0):
        k -= 1
        ans[k] = lo + 1
    ans.sort()
    return ans


print("Ans: ", getSmallestInefficiencies([ 3, 1, 5, 4], 3))
