"""Relative Sort Array
https://leetcode.com/problems/relative-sort-array
"""


class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        freq = {}
        for num in arr1:
            freq[num] = freq.get(num, 0) + 1
        out_index = 0
        for num in arr2:
            count = freq.get(num, 0)
            for i in range(count):
                arr1[out_index] = num
                out_index += 1
            if num in freq:
                del freq[num]
        out = []
        for k, v in freq.items():
            for i in range(v):
                out.append(k)
        return arr1[:out_index] + sorted(out)


def test(arr1, arr2):
    print(Solution().relativeSortArray(arr1, arr2))


test([2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19],  [2, 1, 4, 3, 9, 6])
test([28, 6, 22, 8, 44, 17],  [22, 28, 8, 6])
