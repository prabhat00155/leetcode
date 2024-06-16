"""Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        location = {}
        i = 0
        max_len = 0
        for j in range(len(s)):
            if s[j] in location:
                i = max(i, location[s[j]] + 1)
            location[s[j]] = j
            max_len = max(max_len, j - i + 1)
        return max_len


def test(s):
    print(Solution().lengthOfLongestSubstring(s))


test('abcabcbb')
test('bbbbb')
test('pwwkew')
