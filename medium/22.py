"""Generate Parentheses
https://leetcode.com/problems/generate-parentheses
"""


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        soln = []

        def generate(no, nc, comb):
            if no == 0 and nc == 0:
                soln.append(comb)
            if no < nc:
                generate(no, nc-1, f'{comb})')
            if no > 0:
                generate(no-1, nc, f'{comb}(')

        generate(n, n, '')
        return soln


def test(n):
    print(Solution().generateParenthesis(n))


test(1)
test(2)
test(3)
test(4)
