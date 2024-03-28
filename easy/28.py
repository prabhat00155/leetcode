"""Find the Index of the First Occurrence in a String
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        while i < len(haystack) - len(needle) + 1:
            j = i
            k = 0
            while j < len(haystack) and k < len(needle):
                if haystack[j] != needle[k]:
                    break
                j += 1
                k += 1
            if k == len(needle):
                return i
            i += 1
        return -1


def test(haystack, needle):
    print(Solution().strStr(haystack, needle))


test('sadbutsad', 'sad')
test('leetcode', 'leeto')
