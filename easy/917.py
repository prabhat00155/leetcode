"""Reverse Only Letters
https://leetcode.com/problems/reverse-only-letters
"""


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        i, j = 0, len(s) - 1
        output = ''
        while i < len(s):
            if s[i].isalpha():
                if j >= 0 and s[j].isalpha():
                    output = f'{output}{s[j]}'
                    i += 1
                j -= 1
            else:
                output = f'{output}{s[i]}'
                i += 1
        return output


def test(s: str):
    print(Solution().reverseOnlyLetters(s))


test('ab-cd')
test('a-bC-dEf-ghIj')
test('Test1ng-Leet=code-Q!')
