"""Parsing A Boolean Expression
https://leetcode.com/problems/parsing-a-boolean-expression
"""


class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        operators = []
        operands = []

        def evaluate():
            nonlocal operators, operands

            oper = operators.pop()
            c = operands.pop()
            res = c
            while c != '(':
                if oper == '!':
                    res = not res
                elif oper == '|':
                    res = res or c
                elif oper == '&':
                    res = res and c
                c = operands.pop()
            operands.append(res)

        for c in expression:
            if c == ',':
                continue
            elif c == ')':
                evaluate()
            elif c in ['!', '|', '&']:
                operators.append(c)
            elif c in ['t', 'f']:
                operands.append(True if c == 't' else False)
            else:
                operands.append(c)
        return operands[0]


def test(expression: str) -> bool:
    return Solution().parseBoolExpr(expression)


assert not test('&(|(f))')
assert test('|(f,f,f,t)')
assert test('!(&(f,t))')
