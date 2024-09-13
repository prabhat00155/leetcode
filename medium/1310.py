"""XOR Queries of a Subarray
https://leetcode.com/problems/xor-queries-of-a-subarray
"""


class Solution:
    def xorQueries(
        self, arr: list[int], queries: list[list[int]]
    ) -> list[int]:
        prefix = [0] * len(arr)
        prefix[0] = arr[0]
        for i in range(1, len(arr)):
            prefix[i] = arr[i] ^ prefix[i - 1]
        return list(map(lambda x:
                        prefix[x[1]]
                        if x[0] == 0 else prefix[x[1]] ^ prefix[x[0] - 1],
                        queries))


def test(arr: list[int], queries: list[list[int]]):
    print(Solution().xorQueries(arr, queries))


test([1, 3, 4, 8], [[0, 1], [1, 2], [0, 3], [3, 3]])
test([4, 8, 2, 10], [[2, 3], [1, 3], [0, 0], [0, 3]])
