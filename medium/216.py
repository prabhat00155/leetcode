"""Combination Sum III
https://leetcode.com/problems/combination-sum-iii
"""


class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        solution = set()

        def combine(k, n, cur, start):
            if n <= 0:
                return
            if k == 1 and n <= 9:
                if n not in cur:
                    solution.add(tuple(sorted(cur+(n,))))
                return
            for val in range(start, 10):
                if val not in cur:
                    combine(k-1, n-val, cur+(val,), start+1)

        combine(k, n, (), 1)
        return list(map(lambda x: list(x), solution))


def test(k, n):
    print(Solution().combinationSum3(k, n))


test(3, 9)
test(3, 7)
test(4, 1)
