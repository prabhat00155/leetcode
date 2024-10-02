"""Minimum Remove to Make Valid Parentheses
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses
"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        arr, res = [], ''
        n_open = 0
        for c in s:
            if c != ')':
                arr.append(c)
            if c == '(':
                n_open += 1
            if c == ')' and n_open > 0:
                n_open -= 1
                arr.append(c)
        for a in reversed(arr):
            if n_open > 0 and a == '(':
                n_open -= 1
                continue
            res = f'{a}{res}'
        return res


def test(s: str):
    print(Solution().minRemoveToMakeValid(s))


test('lee(t(c)o)de)')
test('a)b(c)d')
test('))((')
test('())()(((')
