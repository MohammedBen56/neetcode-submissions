class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        used = set([])
        nums.sort()
        for n in nums:
            for r in range(len(res)):
                if tuple(res[r] + [n]) not in used:
                    used.add(tuple(res[r] + [n]))
                    res.append(res[r] + [n])
        return res
        