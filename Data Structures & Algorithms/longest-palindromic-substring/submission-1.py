class Solution:
    def longestPalindrome(self, s: str) -> str:
        resL= 0
        resI=0
        if len(s)==1: return s
        for c in range(len(s)):
            l=c
            r=c
            long=r-l+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                long=r-l+1
                l-=1
                r+=1
            if long >resL:
                resL = long
                resI= c
            l=c
            r=c+1
            long =0
            while l>=0 and r<len(s) and s[l]==s[r]:
                long=r-l+1
                l-=1
                r+=1
            if long >resL:
                resL = long
                resI= c
        if resL % 2 ==0:
            return s[resI-(resL//2)+1:resI+(resL//2)+1]
        else : return s[resI-(resL//2):resI+(+resL//2)+1]





        