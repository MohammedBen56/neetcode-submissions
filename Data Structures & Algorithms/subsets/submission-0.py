class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for n in nums:
            
            for r in range(len(res)):
        
                res.append(res[r] + [n])
        return res
        
        