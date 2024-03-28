"""Length of Last Word
https://leetcode.com/problems/length-of-last-word/
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last = len(s) - 1
        count = 0
        while last >= 0 and s[last] == ' ':
            last -= 1
        while last >= 0 and s[last] != ' ':
            count += 1
            last -= 1
        return count


def test(s):
    print(Solution().lengthOfLastWord(s))


test('Hello World')
test('   fly me   to   the moon  ')
test('')
test('luffy is still joyboy')
