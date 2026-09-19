class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        n = len(nums)
        if target % 2 != 0:
            return False
        m= target // 2
        dp = [False]* (m+1)
        dp[0] = True
        for n in nums:
            for i in range(m,n-1,-1):
                diff = i-n
                dp[i]= dp[i] or dp[diff]

        return dp[m]
