"""Find the Longest Substring Containing Vowels in Even Counts
https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts
"""


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        i, j, longest = 0, 0, 0
        for i in range(len(s)):
            seen = {'a', 'e', 'i', 'o', 'u'}
            for j in range(i, len(s)):
                if s[j] in vowels:
                    if s[j] in seen:
                        seen.remove(s[j])
                    else:
                        seen.add(s[j])
                if len(seen) == len(vowels):
                    longest = max(longest, j-i+1)
            if longest >= len(s) - i:
                break
        return longest


def test(s: str):
    print(Solution().findTheLongestSubstring(s))


test('eleetminicoworoep')
test('leetcodeisgreat')
test('bcbcbc')
test('szy')
