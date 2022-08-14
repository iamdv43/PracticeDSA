def groupAnagrams(strs):
        if len(strs)==0:
            return [[""]]
        ans = {}
        
        for word in strs:
            temp = ''.join(sorted(word))
            if temp in ans:
                ans[temp].append(word)
            else:
                ans[temp] = [word]
        return ans.values()

print("Ans: ", groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
