"""Minimum Add to Make Parentheses Valid
https://leetcode.com/problems/minimum-add-to-make-parentheses-valid
"""


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        n_open, n_close = 0, 0
        for c in s:
            if c == '(':
                n_open += 1
            elif c == ')' and n_open > 0:
                n_open -= 1
            else:
                n_close += 1
        return n_open + n_close


def test(s: str):
    print(Solution().minAddToMakeValid(s))


test('())')
test('(((')
test('()))')
