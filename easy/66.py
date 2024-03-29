"""Plus One
https://leetcode.com/problems/plus-one/
"""


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        carry = 1
        index = len(digits) - 1
        while carry > 0 and index >= 0:
            val = (digits[index] + carry) % 10
            carry = (digits[index] + carry) // 10
            digits[index] = val
            index -= 1
        if carry > 0:
            digits.insert(0, carry)
        return digits


def test(digits):
    print(Solution().plusOne(digits));


test([1, 2, 3])
test([4, 3, 2, 1])
test([9])
test([0])
