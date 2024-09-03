"""Sum of Digits of String After Convert
https://leetcode.com/problems/sum-of-digits-of-string-after-convert
"""


class Solution:
    def getLucky(self, s: str, k: int) -> int:

        def add_digits(num):
            total = 0
            while num > 0:
                total += num % 10
                num = num // 10
            return total

        num = 0
        for c in s:
            power = 2 if ord(c) - ord('a') + 1 >= 10 else 1
            num = num * (10 ** power) + ord(c) - ord('a') + 1

        for _ in range(k):
            num = add_digits(num)
        return num


def test(s: str, k: int):
    print(Solution().getLucky(s, k))


test('iiii', 1)
test('leetcode', 2)
test('zbax', 2)
