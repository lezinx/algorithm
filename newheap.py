from heapq import *


class MedianFinder:
    def __init__(self):
        self.hLow = []  # max heap
        self.hMax = []  # min heap

    def addNum(self, num):
        if len(self.hLow) == len(self.hMax):
            heappush(self.hMax, -heappushpop(self.hLow, -num))
        else:
            heappush(self.hLow, -heappushpop(self.hMax, num))

    def findMedian(self):
        if len(self.hLow) == len(self.hMax):
            return self.hMax[0],-self.hLow[0]
        else:
            return float(self.hMax[0])




heap = MedianFinder()
A = [1,5,6,2,3,4,7,8,9,10]
for i in A:
    heap.addNum(i)
    print(heap.findMedian())

