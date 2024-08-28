"""Valid Palindrome II
https://leetcode.com/problems/valid-palindrome-ii
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:

        def is_valid(i: int, j: int, left: int):
            while i < j:
                if s[i] != s[j]:
                    return is_valid(i+1, j, left-1) or is_valid(
                            i, j-1, left-1) if left > 0 else False
                i += 1
                j -= 1
            return True

        return is_valid(0, len(s)-1, 1)


def test(s: str):
    print(Solution().validPalindrome(s))


test('aba')
test('abca')
test('abc')
