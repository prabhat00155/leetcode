"""Reverse Prefix of Word
https://leetcode.com/problems/reverse-prefix-of-word
"""


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        i = 0
        while word[i] != ch:
            i += 1
        return f'{word[i: 0 : -1]}{word[0]}{word[i+1:]}'


def test(word: str, ch: str) -> str:
    return Solution().reversePrefix(word, ch)


assert test('abcdefd', 'd') == 'dcbaefd'
assert test('xyxzxe', 'z') == 'zxyxxe'
assert test('abcd', 'z') == 'abcd'
