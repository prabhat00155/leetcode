"""Find the Punishment Number of an Integer
https://leetcode.com/problems/find-the-punishment-number-of-an-integer
"""


class Solution:
    def match(self, number, square, divisor):
        if number == square:
            return True
        if number > square or number < square % divisor:
            return False
        return (
            self.match(number-square % divisor, square//divisor, 10)
            or self.match(number, square, divisor*10)
        )

    def is_punishment(self, number):
        square = number * number
        if self.match(number, square, 10):
            return True
        return False

    def punishmentNumber(self, n: int) -> int:
        result = 0
        for i in range(1, n+1):
            if self.is_punishment(i):
                result += i * i
        return result


def test(n):
    print(Solution().punishmentNumber(n))


test(10)
test(37)
