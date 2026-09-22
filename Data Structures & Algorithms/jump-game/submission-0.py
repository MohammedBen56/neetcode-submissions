class Solution:
    def canJump(self, nums: List[int]) -> bool:
        prev=0
        for i in range(len(nums)):
            if prev< i: return False
            prev= max(prev, i+nums[i])
        return True

        