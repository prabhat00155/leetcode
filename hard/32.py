"""Longest Valid Parentheses
https://leetcode.com/problems/longest-valid-parentheses
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        length = 0
        for index, char in enumerate(s):
            if char == '(':
                stack.append(index)
            else:
                stack.pop()
                if not stack:
                    stack.append(index)
                else:
                    length = max(length, index - stack[-1])
        return length


def test(s):
    print(Solution().longestValidParentheses(s))


test('(()')
test(')()())')
test('')
