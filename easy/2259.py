"""Remove Digit From Number to Maximize Result
https://leetcode.com/problems/remove-digit-from-number-to-maximize-result
"""


class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        if not number:
            return number
        last_seen = 0 if number[0] == digit else -1
        for index in range(1, len(number)):
            if number[index - 1] == digit:
                last_seen = index - 1
                if number[index - 1] < number[index]:
                    return number[:index - 1] + number[index:]
        if number[-1] == digit:
            last_seen = len(number) - 1
        return (number if last_seen == -1
                else number[:last_seen] + number[last_seen + 1:])


def test(number, digit):
    print(Solution().removeDigit(number, digit))


test('123', '3')
test('1231', '1')
test('551', '5')
