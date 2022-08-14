def combinationSum(candidates, target):
        res, n = [], len(candidates)
        candidates.sort()

        def dfs(idx, target, path):
            if target < 0:
                return True
            if target == 0:
                res.append(path)
                return False
            for i in range(idx, n):
                if dfs(i, target - candidates[i], path + [candidates[i]]):
                    break
                    
        dfs(0, target, [])
        
        return res 

candidates = [2,3,6,7] 
target = 7
print("Ans: ", combinationSum(candidates, target))