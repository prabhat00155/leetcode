"""Add Strings
https://leetcode.com/problems/add-strings
"""


from collections import deque


class Solution:
    def to_number(self, c):
        return ord(c) - ord('0')

    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1
        output = deque()
        carry = 0

        while i >= 0 or j >= 0 or carry > 0:
            digit1 = self.to_number(num1[i]) if i >= 0 else 0
            digit2 = self.to_number(num2[j]) if j >= 0 else 0
            res = digit1 + digit2 + carry
            digit = res % 10
            carry = res // 10
            output.appendleft(f'{digit}')
            i -= 1
            j -= 1

        return ''.join(output)


def test(num1, num2):
    print(Solution().addStrings(num1, num2))


test('11', '123')
test('456', '77')
test('0', '0')
