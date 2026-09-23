class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        temp= []
        intervals.sort(key = lambda x: x[1])
        res=0
        for i,c in enumerate(intervals):
            if not temp: 
                temp = c
                continue
            if c[0]<temp[1]:
                res+=1
            else: temp = c
        return res



        