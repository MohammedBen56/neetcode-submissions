class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = 1
        count = [1]*len(nums)
        for i in range(1,len(nums)):
            l= i-1
            while l>=0:
                if nums[l]<nums[i]:
                    count[i] = max(count[i], count[l]+1)
                l-=1
            res = max(res, count[i])
        return res
        
        