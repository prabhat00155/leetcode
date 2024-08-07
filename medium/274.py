"""H-Index
https://leetcode.com/problems/h-index
"""


class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort(reverse=True)
        h = 0
        for index, val in enumerate(citations):
            h = max(h, min(index+1, val))
        return h


def test(citations):
    print(Solution().hIndex(citations))


test([0, 1, 0])
test([3, 0, 6, 1, 5])
test([1, 3, 1])
