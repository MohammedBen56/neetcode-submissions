class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        for i, t in enumerate(intervals):
            if not res: res.append(t)
            elif t[0]<=res[-1][1]: res[-1][1]= max(t[1],res[-1][1])
            else: res.append(t)
        return res
        