class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new = []

        for c,i in enumerate(intervals):
            if newInterval[1]<i[0]: 
                new.append(newInterval)
                return new+intervals[c:]
            elif newInterval[0]>i[1]:
                new.append(i)
            else: 
                newInterval= [min(newInterval[0], i[0]) ,max(newInterval[1], i[1])]
                
        new.append(newInterval)
        return new
        