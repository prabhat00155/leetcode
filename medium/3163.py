"""String Compression III

https://leetcode.com/problems/string-compression-iii/description/
"""


class Solution:
    def compressedString(self, word: str) -> str:
        output = ''
        i, count = 0, 0
        cur = word[i]
        while i < len(word):
            if word[i] == cur and count < 9:
                count += 1
                i += 1
            else:
                output = f'{output}{count}{cur}'
                count = 0
                cur = word[i]
        return output if count == 0 else f'{output}{count}{cur}'


def test(word: str) -> str:
    return Solution().compressedString(word)


assert test('abcde') == '1a1b1c1d1e'
assert test('aaaaaaaaaaaaaabb') == '9a5a2b'
