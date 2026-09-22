class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [len(nums)+1]*len(nums)
        dp[-1]=0
        for i in range(len(nums)-2,-1,-1):
            minn = len(nums)+1
            j= i+1
            while j<len(nums) and j < i+1+nums[i]:
                minn = min(minn, dp[j])
                j+=1
            dp[i]= 1+minn
        return dp[0]
        