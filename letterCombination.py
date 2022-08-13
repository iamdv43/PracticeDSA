def letterCombinations(digits):
    ans = []
    if not digits:
        return ans
    mapping = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    ans.append("")
    for i in range(len(digits)):
        x = digits[int(i)]
        while len(ans[0]) == i:
            rm = ans.pop(0)
            for c in mapping[int(x)]:
                ans.append(rm+c)
    return ans

print(letterCombinations('23'))