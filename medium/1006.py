"""Clumsy Factorial
https://leetcode.com/problems/clumsy-factorial
"""


class Solution:
    def clumsy(self, n: int) -> int:
        operators = ['*', '/', '+', '-']
        sums = 0
        operand1 = 0
        operand2 = n
        operator_index = 0
        first_minus = True
        for val in range(n-1, 0, -1):
            if operators[operator_index] == '+':
                sums += val
            elif operators[operator_index] == '*':
                operand2 = operand2 * val
            elif operators[operator_index] == '/':
                operand2 = operand2 // val
            elif operators[operator_index] == '-':
                operand1 = operand2 if first_minus else operand1 - operand2
                first_minus = False
                operand2 = val
            operator_index = (operator_index + 1) % len(operators)
        return operand2 + sums if first_minus else operand1 - operand2 + sums


def test(n):
    print(Solution().clumsy(n))


test(1)
test(10)
test(5)
test(4)
