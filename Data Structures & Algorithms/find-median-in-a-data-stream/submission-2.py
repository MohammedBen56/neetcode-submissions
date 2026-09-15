class MedianFinder:

    def __init__(self):
        self.large = []
        self.small = []
        self.slen = 0
        self.llen=0
        

    def addNum(self, num: int) -> None:
        if not self.large and not self.small:
            heapq.heappush(self.small, -num)
            self.slen+=1
        else:
            if num <= -self.small[0]:
                heapq.heappush(self.small, -num)
                self.slen+=1
            else:
                heapq.heappush(self.large, num)
                self.llen+=1
            while abs(self.slen - self.llen) > 1:
                if self.slen > self.llen:
                    heapq.heappush(self.large, -heapq.heappop(self.small))
                    self.slen-=1
                    self.llen+=1
                else:
                    heapq.heappush(self.small, -heapq.heappop(self.large))
                    self.slen+=1
                    self.llen-=1

        
        

    def findMedian(self) -> float:
        if self.slen == self.llen:
            return (-self.small[0]+self.large[0])/2

        else:
            if self.slen > self.llen:
                return -self.small[0]
            else: return self.large[0]
        
        