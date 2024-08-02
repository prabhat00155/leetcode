"""Find the Prefix Common Array of Two Arrays
https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays
"""


class Solution:
    def findThePrefixCommonArray(
        self, A: list[int], B: list[int]
    ) -> list[int]:
        a_set, b_set = set(), set()
        C = [0] * len(A)
        for i in range(len(A)):
            count = 0
            if A[i] in b_set:
                count += 1
            if B[i] in a_set:
                count += 1
            if A[i] == B[i]:
                count += 1
            a_set.add(A[i])
            b_set.add(B[i])
            C[i] = C[i - 1] + count if i > 0 else count
        return C


def test(A, B):
    print(Solution().findThePrefixCommonArray(A, B))


test([1, 3, 2, 4], [3, 1, 2, 4])
test([2, 3, 1], [3, 1, 2])
