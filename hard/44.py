"""Wildcard Matching
https://leetcode.com/problems/wildcard-matching
"""


class Solution:
    mapper = {}

    def isMatch(self, s: str, p: str) -> bool:
        if (s, p) in self.mapper:
            return self.mapper[(s, p)]
        if s == '':
            if p == '':
                return True
            elif p[0] == '*':
                self.mapper[(s, p)] = self.isMatch(s, p[1:])
                return self.mapper[(s, p)]
            else:
                return False
        if p == '' or (p[0] not in ['?', '*'] and s[0] != p[0]):
            return False
        self.mapper[(s, p)] = (
           self.isMatch(s[1:], p[1:])
           or (p[0] == '*'
               and (self.isMatch(s[1:], p) or self.isMatch(s, p[1:])))
        )
        return self.mapper[(s, p)]


def test(s, p):
    print(Solution().isMatch(s, p))


test('aa', 'a')
test('aa', '*')
test('cb', '?a')
