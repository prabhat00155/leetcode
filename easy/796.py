"""Rotate String
https://leetcode.com/problems/rotate-string
"""


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        i = 0
        new_s = f'{s}{s}'
        while i < len(new_s) - len(goal) + 1:
            end = i + len(goal)
            if goal == new_s[i: end]:
                return True
            i += 1
        return False


def test(s: str, goal: str) -> bool:
    return Solution().rotateString(s, goal)


assert test('abcde', 'cdeab')
assert not test('abcde', 'abced')
