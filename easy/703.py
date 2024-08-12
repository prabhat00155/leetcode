"""Kth Largest Element in a Stream
https://leetcode.com/problems/kth-largest-element-in-a-stream
"""


import heapq


class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.heap = nums
        self.k = k
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) == self.k:
            heapq.heappushpop(self.heap, val)
        else:
            heapq.heappush(self.heap, val)
        return self.heap[0]


obj = KthLargest(3, [4, 5, 8, 2])
print(obj.add(3))
print(obj.add(5))
print(obj.add(10))
print(obj.add(9))
print(obj.add(4))
