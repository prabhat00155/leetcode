"""Length of Last Word
https://leetcode.com/problems/length-of-last-word/
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split()[-1]) if s else 0


def test(s):
    print(Solution().lengthOfLastWord(s))


test('Hello World')
test('   fly me   to   the moon  ')
test('')
test('luffy is still joyboy')
