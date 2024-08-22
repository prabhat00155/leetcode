"""Basic Calculator
https://leetcode.com/problems/basic-calculator
"""


class Solution:
    def calculate(self, s: str) -> int:
        operators, operands = [], []

        def evaluate():
            nonlocal operators, operands
            while operators and operators[-1] in ['+', '-']:
                num1 = operands.pop()
                num0 = operands.pop()
                op = operators.pop()
                operands.append(num0+num1 if op == '+' else num0-num1)

        i, operands_seen = 0, False
        while i < len(s):
            if s[i] in ['+', '-', '(']:
                if s[i] == '(':
                    operands_seen = False
                if s[i] == '-' and not operands_seen:
                    operands.append(0)
                operators.append(s[i])
                i += 1
            elif s[i] == ')':
                while operators:
                    if operators[-1] == '(':
                        operators.pop()
                        break
                    else:
                        evaluate()
                evaluate()
                i += 1
            elif s[i] == ' ':
                i += 1
            else:
                num = 0
                operands_seen = True
                while i < len(s) and '0' <= s[i] <= '9':
                    num = num * 10 + (ord(s[i]) - ord('0'))
                    i += 1
                operands.append(num)
                evaluate()
        evaluate()
        return operands.pop()


def test(s: str):
    print(Solution().calculate(s))


test('1 + 1')
test(' 2-1 + 2 ')
test('(1+(4+5+2)-3)+(6+8)')
test('1-(     -2)')
test('- (3 + (4 + 5))')
test('(7)-(0)+(4)')
