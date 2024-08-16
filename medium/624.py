"""Maximum Distance in Arrays
https://leetcode.com/problems/maximum-distance-in-arrays
"""


import heapq


class Solution:
    def maxDistance(self, arrays: list[list[int]]) -> int:
        min_heap, max_heap = [], []
        for index, arr in enumerate(arrays):
            heapq.heappush(min_heap, (arr[0], index))
            heapq.heappush(max_heap, (-arr[-1], index))
        minima1, min_index1 = heapq.heappop(min_heap)
        minima2, min_index2 = heapq.heappop(min_heap)
        maxima1, max_index1 = heapq.heappop(max_heap)
        maxima2, max_index2 = heapq.heappop(max_heap)
        return abs(minima1+maxima1) if min_index1 != max_index1 else max(
            abs(minima1+maxima2),
            abs(minima2+maxima1)
        )


def test(arrays):
    print(Solution().maxDistance(arrays))


test([[1, 2, 3], [4, 5], [1, 2, 3]])
test([[1], [1]])
