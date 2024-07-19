"""Add to Array-Form of Integer
https://leetcode.com/problems/add-to-array-form-of-integer
"""


from collections import deque


class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        carry, index = 0, len(num) - 1
        output = deque()
        while index >= 0:
            val = num[index] + k % 10 + carry
            carry = val // 10
            val = val % 10
            k = k // 10
            output.appendleft(val)
            index -= 1
        while k > 0:
            val = k % 10 + carry
            carry = val // 10
            val = val % 10
            output.appendleft(val)
            k = k // 10
        if carry > 0:
            output.appendleft(carry)
        return list(output)


def test(num, k):
    print(Solution().addToArrayForm(num, k))


test([1, 2, 0, 0], 34)
test([2, 7, 4], 181)
test([2, 1, 5], 806)
