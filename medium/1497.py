"""Check If Array Pairs Are Divisible by k
https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k
"""


class Solution:
    def canArrange(self, arr: list[int], k: int) -> bool:
        mapper = {i: 0 for i in range(k)}

        for num in arr:
            mapper[num % k] += 1
        if mapper[0] % 2 != 0:
            return False
        for i in range(1, k//2+1):
            if mapper[i] != mapper[k - i]:
                return False
            if i == k - i and mapper[i] % 2 != 0:
                return False
        return True


def test(arr: list[int], k: int):
    print(Solution().canArrange(arr, k))


test([1, 2, 3, 4, 5, 10, 6, 7, 8, 9], 5)
test([1, 2, 3, 4, 5, 6], 7)
test([1, 2, 3, 4, 5, 6], 10)
