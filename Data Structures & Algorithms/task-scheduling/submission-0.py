class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        values = Counter(tasks)
        heap = [-i for i in values.values()]
        heapq.heapify(heap)
        q = deque()
        time =0

        while heap or q:
            time +=1
            if heap:
                c = heapq.heappop(heap) +1
                if c != 0:
                    q.append((c,time+n))
            if q:
                if time >= q[0][1]:
                    heapq.heappush(heap, q.popleft()[0])
        

        
        return time

        