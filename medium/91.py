"""Decode Ways
https://leetcode.com/problems/decode-ways
"""


MINIMA = 1
MAXIMA = 26


class Solution:
    mapper = {}

    def is_valid(self, s):
        if s[0] == '0':
            return False
        return True if MINIMA <= int(s) <= MAXIMA else False

    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        if s not in self.mapper:
            total = 1 if self.is_valid(s) else 0
            if self.is_valid(s[0]):
                total += self.numDecodings(s[1:])
            if len(s) > 2 and self.is_valid(s[0:2]):
                total += self.numDecodings(s[2:])
            self.mapper[s] = total
        return self.mapper[s]


def test(s):
    print(Solution().numDecodings(s))


test('12')
test('226')
test('06')
