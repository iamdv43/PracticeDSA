def goodString(N,Q,S,arr,ranges):
    count = 0
    for i in ranges:
        sub = S[i[0]-1:i[1]]
        for c in sub:
            if sub.count(c) > 1:
                sub = sub.replace(c, '')
                count += 1      
        S.replace(S[i[0]-1:i[1]], sub)     
    return count

N = 5
Q = 2
S = "aaaaa"
arr = [2,4,1,3,5]
ranges = [[1,2],[4,5]]
print("Ans: ", goodString(N,Q,S,arr,ranges) )

