class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxx = nums[0]
        cur= maxx
        for i in range(1,len(nums)):
            cur = max(nums[i], cur+nums[i])
            maxx = max(cur, maxx)
        return maxx