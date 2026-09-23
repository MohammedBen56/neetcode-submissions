class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index= {}
        for i in range(len(s)):
            last_index[s[i]]=i
        start=0
        end=0
        res=[]
        for i in range(len(s)):
            end = max(end, last_index[s[i]])
            if i == end:
                res.append(end-start+1)
                start=i+1
        return res
        