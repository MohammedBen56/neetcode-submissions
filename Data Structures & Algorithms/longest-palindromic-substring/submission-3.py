class Solution:
    def longestPalindrome(self, s: str) -> str:
        resL= 0
        resI=0
        new= '#'+'#'.join(s)+'#'
        if len(s)==1: return s
        for c in range(len(new)):
            l=c
            r=c
            while l>=0 and r<len(new) and new[l]==new[r]:
                long=r-l+1
                l-=1
                r+=1
            if long >resL:
                resL = long
                resI= l+1
        return s[resI//2:(resI//2)+(resL//2)]





        