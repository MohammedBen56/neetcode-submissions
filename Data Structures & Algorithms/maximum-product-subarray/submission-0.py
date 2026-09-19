class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        n= len(nums)
        pre = su = 0
        for i in range(n):
            pre = nums[i] * (pre or 1)
            su = nums[n-i-1] * (su or 1)
            res = max(res, max(pre, su))
        return res
        