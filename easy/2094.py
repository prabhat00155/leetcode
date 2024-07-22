"""Finding 3-Digit Even Numbers
https://leetcode.com/problems/finding-3-digit-even-numbers
"""


class Solution:
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        res = set()
        for i in range(len(digits)-2):
            for j in range(i+1, len(digits)-1):
                for k in range(j+1, len(digits)):
                    nums = [
                        digits[i] * 100 + digits[j] * 10 + digits[k],
                        digits[i] * 100 + digits[k] * 10 + digits[j],
                        digits[j] * 100 + digits[i] * 10 + digits[k],
                        digits[j] * 100 + digits[k] * 10 + digits[i],
                        digits[k] * 100 + digits[i] * 10 + digits[j],
                        digits[k] * 100 + digits[j] * 10 + digits[i],
                    ]
                    for num in nums:
                        if num >= 100 and num % 2 == 0:
                            res.add(num)
        return sorted(list(res))


def test(digits):
    print(Solution().findEvenNumbers(digits))


test([2, 2, 8, 8, 2])
test([2, 1, 3, 0])
test([3, 7, 5])
