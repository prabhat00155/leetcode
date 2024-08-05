"""Kth Distinct String in an Array
https://leetcode.com/problems/kth-distinct-string-in-an-array
"""


class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        seen = {}
        for s in arr:
            seen[s] = seen.get(s, 0) + 1
        count = 0
        for s in arr:
            if seen[s] == 1:
                count += 1
                if count == k:
                    return s
        return ''


def test(arr: list[str], k: int):
    print(Solution().kthDistinct(arr, k))


test(["d", "b", "c", "b", "c", "a"], 2)
test(["aaa", "aa", "a"], 1)
test(["a", "b", "a"], 3)
