class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [1]*(len(s)+1)
        if s[0]!= '0':dp[0] = 1 
        else: return 0
        def isvalid(w):
            if int(w)>=10 and int(w)<27:
                return 1
            else: return 0
        for i in range(len(s)-1,-1,-1):
            if s[i]=='0':
                dp[i]=0
            else:
                dp[i]=dp[i+1]
            
            if isvalid(s[i:i+2]): dp[i]+= dp[i+2]
        
             
        return dp[0]
        
        