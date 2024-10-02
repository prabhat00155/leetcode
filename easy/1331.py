"""Rank Transform of an Array
https://leetcode.com/problems/rank-transform-of-an-array
"""


class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        sorted_arr = sorted(arr)
        ranks, output = {}, []
        cur = 1
        i, j = 0, 0
        while i < len(sorted_arr) and j < len(sorted_arr):
            if sorted_arr[i] == sorted_arr[j]:
                j += 1
            else:
                ranks[sorted_arr[i]] = cur
                i, j = j, j + 1
                cur += 1
        if i < len(sorted_arr):
            ranks[sorted_arr[i]] = cur
        for a in arr:
            output.append(ranks[a])
        return output


def test(arr: list[int]):
    print(Solution().arrayRankTransform(arr))


test([40, 10, 20, 30])
test([100, 100, 100])
test([37, 12, 28, 9, 100, 56, 80, 5, 12])
