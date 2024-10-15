"""Separate Black and White Balls
https://leetcode.com/problems/separate-black-and-white-balls
"""


class Solution:
    def minimumSteps(self, s: str) -> int:
        if len(s) <= 1:
            return 0
        arr = list(s)

        swaps = 0
        i, j = 0, 1

        while i < len(arr) and j < len(arr):
            if arr[i] == '1' and arr[j] == '0':
                swaps = swaps + j - i
                arr[i], arr[j] = arr[j], arr[i]
            if arr[i] == '0':
                i += 1
            j += 1
        return swaps


def test(s: str):
    print(Solution().minimumSteps(s))


test('101')
test('100')
test('0111')
test('0011011')
