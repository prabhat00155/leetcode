"""Valid Parentheses
https://leetcode.com/problems/valid-parentheses
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        mapper = {
            '(': ')',
            '{': '}',
            '[': ']',
        }
        for c in s:
            if c in mapper.keys():
                stk.append(c)
            elif len(stk) == 0 or c != mapper[stk.pop()]:
                return False
        return len(stk) == 0


def test(s):
    print(Solution().isValid(s))


test('()')
test('}()')
test('({})[]')
