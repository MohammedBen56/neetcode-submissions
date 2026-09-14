class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap =[ ]
        count= 0
        for p in points:
            val = math.sqrt(p[0]**2+p[1]**2)
            heapq.heappush(heap,(-val,p))
            count +=1
            if count>k:
                heapq.heappop(heap)
                count-=1

        res = []
        while heap:
            res.append(heapq.heappop(heap)[1])
        return res

        