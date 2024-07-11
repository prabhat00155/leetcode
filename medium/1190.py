"""Reverse Substrings Between Each Pair of Parentheses
https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses
"""


class Solution:
    def reverseParentheses(self, s: str) -> str:
        stk = []
        for c in s:
            if c == ')':
                string = ''
                while len(stk) > 0:
                    item = stk.pop()
                    if item == '(':
                        break
                    string = f'{item}{string}'
                stk.append(string[::-1])
            else:
                stk.append(c)
        return ''.join(stk) if len(stk) > 0 else ''


def test(s):
    print(Solution().reverseParentheses(s))


test('(abcd)')
test('(u(love)i)')
test('(ed(et(oc))el)')
