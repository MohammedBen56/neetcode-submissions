class Solution:
    def compress(self, chars: list[str]) -> int:
        s= ""
        l=""
        count=0
        chars.append("")
        for c in chars:
            if c==l:
                count+=1
            else:
                if count>1:
                    s+=str(count)
                s+=c
                l=c
                count=1
        chars.pop()

        chars[:] = s
        return len(s)
        
            
        