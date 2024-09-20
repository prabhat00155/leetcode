"""Remove All Adjacent Duplicates In String
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string
"""


class Solution:
    def removeDuplicates(self, s: str) -> str:
        i = 1
        while i < len(s):
            if s[i] == s[i - 1]:
                s = s[:i - 1] + s[i + 1:]
                i = max(1, i-1)
            else:
                i += 1
        return s


def test(s: str):
    print(Solution().removeDuplicates(s))


test('abbaca')
test('azxxzy')
