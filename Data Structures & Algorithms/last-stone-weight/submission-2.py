class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1 * i for i in stones]
        heapq.heapify(stones)
        while stones:
            x = heapq.heappop(stones)
            if not stones: return -x
            y = heapq.heappop(stones)
            if x == y : continue
            else: heapq.heappush(stones, -abs(x-y))
        return 0
        