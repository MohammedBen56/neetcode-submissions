class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s= sum(nums)
        if (s + target) % 2 != 0 or abs(target) > s: 
            return 0
        new = (s+target)//2
        dp = [0]*(new+1)
        dp[0]=1
        for n in nums:
            for i in range(new,n-1,-1):
                dp[i]+=dp[i-n]
        print(dp)
        return dp[-1]
        