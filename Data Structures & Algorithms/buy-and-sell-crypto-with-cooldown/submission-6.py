class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp=[[0]*len(prices) for _ in range(2)]
        dp[1][-1]= prices[-1]
        if len(prices)==1: return 0
        dp[1][-2]= max(prices[-2],prices[-1])
        dp[0][-2]= max(dp[1][-1]-prices[-2], dp[0][-1])
        for i in range(len(prices)-3,-1,-1):
            dp[0][i]= max(dp[0][i+1], dp[1][i+1]-prices[i])
            dp[1][i]= max(prices[i]+dp[0][i+2], dp[1][i+1])
        return max(0,dp[0][0])