################################# BRUTE FORECE #####################################

def restoreIp(s):
    ret = []
    r = [1, 2, 3]
    for a in r:
        for b in r:
            for c in r:
                for d in r:
                    if a + b + c + d != len(s):
                        continue
                    nums_str = [s[:a], s[a:a+b], s[a+b:a+b+c], s[a+b+c:]]
                    nums_int = [int(x) for x in nums_str if int(x)<256]
                    if len(nums_int) != 4:
                        continue
                    nums_str_without_prefix = [str(x) for x in nums_int]
                    if nums_str != nums_str_without_prefix:
                        continue
                    ret.append('.'.join(nums_str))

    return ret

print("Ans: ", restoreIp("25525511135"))

####################################### DFS #############################################

def r(s):
    ans = []

    def helper( s, k, temp):
        if len(s) > k*3:
            return
        if k == 0:
            ans.append(temp[:])
        else:
            remaining_numbers = len(s)-k+1
            for i in range(min(3,remaining_numbers)):
                if i==2 and int(s[:3]) > 255 or i > 0 and s[0] == '0':
                    continue
                helper( s[i+1:], k-1, temp+[s[:i+1]])

    helper(s, 4, [])
    return ['.'.join(x) for x in ans]


print("Ans: ", r("25525511135"))