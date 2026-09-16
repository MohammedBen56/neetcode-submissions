class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def helper(start, target, path):
            if target ==0:
                res.append(list(path))
                return
            if target < 0:
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                helper(i+1, target - candidates[i], path)
                path.pop()
            
        helper(0, target, [])
        return res