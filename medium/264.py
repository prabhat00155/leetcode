"""Ugly Number II
https://leetcode.com/problems/ugly-number-ii
"""


import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap, seen, count = [], set(), 0
        heapq.heappush(heap, 1)
        seen.add(1)
        factors = [2, 3, 5]
        while count < n:
            num = heapq.heappop(heap)
            for f in factors:
                if num * f not in seen:
                    heapq.heappush(heap, num*f)
                    seen.add(num*f)
            count += 1
        return num


def test(n: int):
    print(Solution().nthUglyNumber(n))


test(10)
test(1)
