"""Minimum ASCII Delete Sum for Two Strings
https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings
"""


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        mapper = {}

        def find(index1, index2):
            if index1 == len(s1) and index2 == len(s2):
                return 0
            if (
                index1 < len(s1) and index2 < len(s2)
                and s1[index1] == s2[index2]
            ):
                return find(index1+1, index2+1)
            if (index1, index2) not in mapper:
                v1, v2 = float('inf'), float('inf')
                if index1 < len(s1):
                    v1 = ord(s1[index1]) + find(index1+1, index2)
                if index2 < len(s2):
                    v2 = ord(s2[index2]) + find(index1, index2+1)
                mapper[(index1, index2)] = min(v1, v2)
            return mapper[(index1, index2)]

        return find(0, 0)


def test(s1, s2):
    print(Solution().minimumDeleteSum(s1, s2))


test('sea', 'eat')
test('delete', 'leet')
