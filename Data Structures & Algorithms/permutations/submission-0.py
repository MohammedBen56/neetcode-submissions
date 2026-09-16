class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = set()
        def helper(path):
            if len(path) == len(nums):
                res.append(list(path))
                return
            
            for i in range(len(nums)):
                if nums[i] in visited: continue
                visited.add(nums[i])
                path.append(nums[i])
                helper(path)
                visited.remove(nums[i])
                path.pop()

        helper([])
        return res